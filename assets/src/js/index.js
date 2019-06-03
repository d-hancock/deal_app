import React from 'react';
import ReactDOM from 'react-dom';
import Test from "./components/Test.jsx";


class App extends React.Component {
    render() {

        return (
            <div>
                <h1>Testing React</h1>
                <Test/>
            </div>
        )
    }
}

ReactDOM.render(<App/>, document.getElementById('react-test'));
