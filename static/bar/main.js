import * as THREE from 'three';
import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader';
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls';
import GUI from 'lil-gui';

let renderer, scene, camera, obj;
let mixer, gui, mainAction;
let isAnimating = false;

export function loadModel() {
    
    scene = new THREE.Scene();
    scene.background = new THREE.Color( 0x87CEFA );
    camera = new THREE.PerspectiveCamera(50, window.innerWidth/ window.innerHeight, 0.1, 1000);
    camera.position.z = 25;

    const dirLight = new THREE.DirectionalLight(0xffffff, 1);
    dirLight.position.set(1, 1, 1);
    scene.add(dirLight);
    const ambLight = new THREE.AmbientLight(0x333333);
    scene.add(ambLight);
    
    const canvas = document.querySelector("canvas");
    renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true, canvas:canvas});
    renderer.setSize(window.innerWidth, window.innerHeight);
    renderer.setPixelRatio(window.devicePixelRatio);

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

    const loader = new GLTFLoader();
    loader.load(window.modelPath, (gltf) => {
    obj = gltf.scene;
    obj.scale.set(1, 1, 1);
    obj.position.set(0, -3, 0);
    scene.add(obj);

    if (gltf.animations.length > 0) {
    mixer = new THREE.AnimationMixer(obj);
    mainAction = mixer.clipAction(gltf.animations[0]);
    mainAction.play();
    mainAction.paused = true;
    mixer.update(0);
}
     animate();
    });

}

let clock = new THREE.Clock(); 

function animate() {
    requestAnimationFrame(animate);
    const delta = clock.getDelta();
    if(mixer && isAnimating) {
        mainAction.paused = false;
        mainAction.play();
        mixer.update(delta);
    }

    renderer.render(scene, camera);
}

export function startAnimation() {
    isAnimating=true;
        if (mixer) {
            mixer.timeScale=1.0;
        }
    }

export function stopAnimation()
    {
    isAnimating=false;
    if(mainAction){
        mainAction.paused = true;
    }
    }

export function reverseanimation(){

    console.log("reverse function called.");
    isAnimating=true;
    
    if(mainAction){
            mainAction.paused = false;
            mainAction.play();
        }
    mixer.timeScale = -mixer.timeScale;
    }

export function slowdown() {
    isAnimating=true;

    if(mainAction){
            mainAction.paused = false;
            mainAction.play();
        }

    console.log("slowdown function called.");
    if (mixer) {
        console.log("Mixer found:", mixer);
        mixer.timeScale = 0.5;
    }else{
        console.warn('Mixer is not initiated.');
    }
}


    