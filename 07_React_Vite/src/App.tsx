import "./App.css";
import viteLogo from "/vite.svg";

//TASK 1:
//TODO: Create a new component called "Header"
//TODO: Add the Header component to the App component
//TODO: Do your best to match the styling of src/images/Header-Sample.png
//      Feel free to use any styling method you'd like, we have CSS, SCSS and tailwind installed
//      You can add additional libraries if you'd like, but it's not necessary
//      You can use an icon library or just use lower case letters for the icons
//      No need to make a functional component for the search bar or dropdowns
//      Light or dark mode

function App() {
  return (
    <>
      <div>
        <a href="https://vite.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
      </div>
      <h1>Vite + React</h1>
    </>
  );
}

export default App;
