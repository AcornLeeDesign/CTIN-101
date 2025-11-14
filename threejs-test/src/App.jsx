import React, { useEffect, useRef } from 'react';
import * as THREE from 'three';
import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader';
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls';
import './App.css';

const App = () => {
  const mountRef = useRef(null);

  useEffect(() => {
    // Scene
    const scene = new THREE.Scene();
    scene.background = new THREE.Color(0x000000);

    // Camera
    const camera = new THREE.PerspectiveCamera(
      75,
      window.innerWidth / window.innerHeight,
      0.1,
      1000
    );
    camera.position.set(0, 1.5, 5);

    // Renderer
    const renderer = new THREE.WebGLRenderer({ antialias: true });
    renderer.setSize(window.innerWidth, window.innerHeight);

    // Remove any leftover canvases (from prior Strict Mode runs)
    if (mountRef.current) {
      while (mountRef.current.firstChild) {
        mountRef.current.removeChild(mountRef.current.firstChild);
      }
      mountRef.current.appendChild(renderer.domElement);
    }

    // Lighting
    const ambientLight = new THREE.AmbientLight(0xffffff, 0.6);
    scene.add(ambientLight);

    const directionalLight = new THREE.DirectionalLight(0xffffff, 1.5);
    directionalLight.position.set(5, 10, 7.5);
    scene.add(directionalLight);

    // OrbitControls
    const controls = new OrbitControls(camera, renderer.domElement);
    controls.enableDamping = true;
    controls.dampingFactor = 0.05;

    // Load model from /public
    const loader = new GLTFLoader();
    loader.load(
      '/characterface.glb',
      (gltf) => {
        const model = gltf.scene;
        model.scale.set(1.5, 1.5, 1.5);
        model.position.set(0, 0, 0);
        scene.add(model);
      },
      undefined,
      (error) => {
        console.error('Error loading GLB model:', error);
      }
    );

    // Animation loop
    const animate = () => {
      requestAnimationFrame(animate);
      controls.update();
      renderer.render(scene, camera);
    };
    animate();

    // Handle resize
    const handleResize = () => {
      camera.aspect = window.innerWidth / window.innerHeight;
      camera.updateProjectionMatrix();
      renderer.setSize(window.innerWidth, window.innerHeight);
    };
    window.addEventListener('resize', handleResize);

    // Cleanup (Strict Mode–safe)
    return () => {
      window.removeEventListener('resize', handleResize);
      controls.dispose();
      renderer.dispose();

      if (
        renderer.domElement &&
        renderer.domElement.parentNode === mountRef.current
      ) {
        renderer.domElement.parentNode.removeChild(renderer.domElement);
      }
    };
  }, []);

  return (
    <div ref={mountRef} style={{ width: '100vw', height: '100vh' }}>
      {/* Three.js canvas mounts here */}
    </div>
  );
};

export default App;
