import * as THREE from 'three';
import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader';
import {OrbitControls} from 'https://unpkg.com/three@0.126.0/examples/jsm/controls/OrbitControls.js';
import {GUI} from 'http://unpkg.com/three@0.126.0/examples/jsm/libs/dat.gui.module.js';

let animationId = null;
let renderer, scene, camera, obj001;
let mixer = null;
let mixerTime = 0; // 停止時の時間を保持
let isAnimating = false;
let gui = null;

export function startAnimation() {
    if (isAnimating) return;
    isAnimating = true;

    //モデルをロード
    const loader = new GLTFLoader();
    loader.load(window.modelPath, (gltf) => {
    obj001 = gltf.scene;
    obj001.scale.set(1, 1, 1);
    obj001.position.set(0, -3, 0);
    scene.add(obj001);

    if (gltf.animations.length > 0) {
    mixer = new THREE.AnimationMixer(obj001);
    const action = mixer.clipAction(gltf.animations[0]);//clip action ,Returns an AnimationAction for the passed clip
    action.play(); //tells the mixer to activate the action.
    mixer.setTime(mixerTime);//Sets the global mixer to a specific time and updates the animation accordingly.
    }

    });
    
    // シーン・カメラ
    scene = new THREE.Scene();
    scene.background = new THREE.Color( 0x87CEFA );
    camera = new THREE.PerspectiveCamera(50, window.innerWidth/ window.innerHeight, 0.1, 1000);
    camera.position.z = 25;
    
    // ライト
    const dirLight = new THREE.DirectionalLight(0xffffff, 1);
    dirLight.position.set(1, 1, 1);
    scene.add(dirLight);

    const ambLight = new THREE.AmbientLight(0x333333);
    scene.add(ambLight);

    // レンダラー
    // HTML側とキャンバスを結び付け
    const canvasContainer = document.getElementById("three-canvas");
    renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true, canvasContainer });
    renderer.setSize(window.innerWidth, window.innerHeight);
    renderer.setPixelRatio(window.devicePixelRatio);
    
    // レンダラーの出力をhtmlに追加する
    canvasContainer.innerHTML='';
    canvasContainer.appendChild(renderer.domElement);//domelement is a canvas where the renderer draws its output

        //マウスで視点変更
    const controls = new OrbitControls(camera, renderer.domElement);

    if (!gui){
    const settings = {
        resetCamera: function() {
            controls.dispose();
            controls.update();
            camera.position.set(10,10,10);
        }
    };
    
    gui = new GUI();
    gui.add(settings, 'resetCamera');
    gui.open();
    }

    let clock = new THREE.Clock(); 
    // アニメーション
    function render() {
        animationId = requestAnimationFrame(render);//引数には繰り返し処理をしたい関数名を指定します。
        const delta = clock.getDelta();
        
        if(mixer) { 
            mixer.update(delta);
            mixerTime = mixer.time;//The global mixer time
        }
        controls.update();
        renderer.render(scene, camera);
    }

    render();
}

export function stopAnimation()
    {
    if (animationId !== null) {
        cancelAnimationFrame(animationId);
        animationId = null;
        isAnimating = false;
    }
}

export function reverseanimation()

    {
    console.log("reverse function called.");
    mixer.timeScale = -mixer.timeScale;
    }

export function slowdown() {
    console.log("slowdown function called.");
    if (mixer) {
        console.log("Mixer found:", mixer);
        mixer.timeScale = 0.5;
    }else{
        console.warn('Mixer is not initiated.');
    }
}
