import React from 'react';
import ReactDOM from 'react-dom';
import RevMaster from './components/Rev/RevMaster.jsx';
import '../../src/css/App.css';

const data = {
    "vehicle": "F-150",
    "trim": [
        {
            "name": "XLT",
            "msrp": "40,000",
            "imgurl": "https://image.shutterstock.com/image-illustration/cartoon-car-gives-thumbs-260nw-274971374.jpg",
            "offers": {"savings": "400", "finance": "0.0", "lease": "412"}
        },
        {
            "name": "Lariat",
            "msrp": "45,000",
            "imgurl": "https://image.shutterstock.com/image-illustration/cartoon-car-gives-thumbs-260nw-274971374.jpg",
           "offers": {"savings": "420", "finance": "1.0", "lease": "452"}
        },
        {
            "name": "King Ranch",
            "msrp": "47,000",
            "imgurl": "https://image.shutterstock.com/image-illustration/cartoon-car-gives-thumbs-260nw-274971374.jpg",
           "offers": {"savings": "430", "finance": "4.0", "lease": "512"}
        },
        {
            "name": "Raptor",
            "msrp": "60,000",
            "imgurl": "https://image.shutterstock.com/image-illustration/cartoon-car-gives-thumbs-260nw-274971374.jpg",
           "offers": {"savings": "440", "finance": "2.0", "lease": "422"}
        },
    ]
};

class App extends React.Component {
    render() {

        return (
            <div>
                <h1>Testing Rev</h1>
                <RevMaster data={data}/>
            </div>
        )
    }
}

ReactDOM.render(<App/>, document.getElementById('react-app'));