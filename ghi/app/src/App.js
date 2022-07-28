import { BrowserRouter, Routes, Route } from 'react-router-dom';
import MainPage from './MainPage';
import Nav from './Nav';
import HatForm from './HatForm';


function App() {
  return (
    <BrowserRouter>
      <Nav />
      <div className="container">
        <Routes>
          <Route path="/" element={<MainPage />} />
        
        {/* <Route path="hat"> */}
          <Route path="/hats" element={<HatForm />} />
        {/* </Route> */}
        </Routes>

      </div>
    </BrowserRouter>
  );
}

export default App;
