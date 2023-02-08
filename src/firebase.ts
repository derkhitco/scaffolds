import { initializeApp } from 'firebase/app';
import { getFunctions, connectFunctionsEmulator } from 'firebase/functions';

// Update this to the actual config
const firebaseConfig = {
  apiKey: "AIzaSyDxbVz5LkiLGeVtsH9D-eOvrK7ynIuRSBY",
  authDomain: "kerk-enzo.firebaseapp.com",
  projectId: "kerk-enzo",
  databaseURL: "https://kerk-enzo-default-rtdb.europe-west1.firebasedatabase.app",
  storageBucket: "kerk-enzo.appspot.com",
  messagingSenderId: "611591459233",
  appId: "1:611591459233:web:a367389d13e2362c2c3be0",
  measurementId: "G-LQ7HK2DC3X"
};

const app = initializeApp(firebaseConfig);
const functions = getFunctions(app);

if (process.env.NODE_ENV === 'local') {
  connectFunctionsEmulator(functions, 'localhost', 5001);
}

export { firebaseConfig, functions, app }