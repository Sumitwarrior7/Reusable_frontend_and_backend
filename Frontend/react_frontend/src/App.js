import Home from "./pages/home";
import ResultPage from "./pages/result";
import { Routes, Route} from 'react-router-dom'

function App() {
  return (
    <div className="App">
      <Routes>
        <Route exact path="/" element={<Home />} />
        <Route exact path="/result" element={<ResultPage />} />
      </Routes>
    </div>
  );
}

export default App;
