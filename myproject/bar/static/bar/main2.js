import * as THREE from 'https://unpkg.com/three@0.162.0/build/three.module.js';
import { GLTFLoader } from './node_modules/three/examples/jsm/loaders/GLTFLoader.js';



let animationId = null;
let renderer, scene, camera, obj001, mixer, clock; // clockを追加
let isAnimating = false;

export function startAnimation() {
    if (isAnimating) return;
    isAnimating = true;

    const C_WIDTH = window.innerWidth;
    const C_HEIGHT = window.innerHeight;

    // シーン・カメラ
    scene = new THREE.Scene();
    camera = new THREE.PerspectiveCamera(50, C_WIDTH / C_HEIGHT, 0.1, 1000);
    camera.position.z = 30;

    // レンダラー
    renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true });
    renderer.setSize(C_WIDTH, C_HEIGHT);
    renderer.setPixelRatio(window.devicePixelRatio);

    // HTML側とキャンバスを結び付け  
    const canvasContainer = document.getElementById("three-canvas");
    canvasContainer.appendChild(renderer.domElement);

    // ライト
    const dirLight = new THREE.DirectionalLight(0xffffff, 1);
    dirLight.position.set(1, 1, 1);
    scene.add(dirLight);

    const ambLight = new THREE.AmbientLight(0x333333);
    scene.add(ambLight);

    const loader = new GLTFLoader();

    let mixer = null

    loader.load(window.modelPath, (gltf) => {
    obj001 = gltf.scene;
    obj001.scale.set(1, 1, 1);
    obj001.position.set(0, 0, 0);
    scene.add(obj001);
}, );
    mixer = new THREE.AnimationMixer(obj001);
    if(gltf.animations.length>0){
        const action = mixer.clipAction(gltf.animations[0]);
        action.play();
    }

    animate();

    // リサイズ対応
    window.addEventListener("resize", handleResize);
    function handleResize() {
        const width = window.innerWidth;
        const height = window.innerHeight;
        camera.aspect = width / height;
        camera.updateProjectionMatrix();
        renderer.setSize(width, height);
    }

    

    // アニメーション
    function animate() {
        animationId = requestAnimationFrame(animate);
        if(mixer) mixer.update(delta);
        renderer.render(scene, camera);
        
    }

    animate();
}


export function stopAnimation()
    {
    if (animationId !== null) {
        cancelAnimationFrame(animationId);
        animationId = null;
    }
}



