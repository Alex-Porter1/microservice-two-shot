import React from 'react';

class HatForm extends React.Component{
    constructor(props) {
        super(props)
        this.state = {
            fabric:"",
            name:"",
            color:"",
            picture_url:"",
            locations:[]

        };

        this.handleFieldChange = this.handleFieldChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }


    async handleSubmit(event) {
        event.preventDefault();
        const data = {...this.state};
        delete data.locations;
        console.log(data);

        const hatUrl = 'http://localhost:8090/api/hats/';
        
        const fetchConfig = {
        method: "post",
        body: JSON.stringify(data),
        headers: {
            'Content-Type': 'application/json',
        },
        };
        
        
        const response = await fetch(hatUrl, fetchConfig);
        if (response.ok) {
        const newHat = await response.json();
        console.log(newHat);

        const cleared = {
            fabric:"",
            name:"",
            color:"",
            style:"",
            picture_url:"",
            location:""

          };
        this.setState(cleared);

    }
}

handleFieldChange(event) {
    const value = event.target.value;
    this.setState({[event.target.id]: value})
}

async componentDidMount(){
    const url = 'http://localhost:8100/api/locations/';
    const response = await fetch(url);
    if (response.ok) {
        const data = await response.json();
        this.setState({locations: data.locations});
        
        
    
        // const selectTag = document.getElementById('location');
        // for (let location of data.locations) {
        //     let option = document.createElement("option");
        //     option.value = location.id
        //     option.innerHTML = location.name
        //     selectTag.appendChild(option)


        // }

    }}

    render(){
        return(

            <div className="row">
            <div className="offset-3 col-6">
              <div className="shadow p-4 mt-4">
                <h1>Create a new conference</h1>
                <form onSubmit={this.handleSubmit} id="create-hat-form">
                  <div className="form-floating mb-3">
                    <input onChange={this.handleFieldChange} value={this.state.name} placeholder="Name" required type="text" name="name" id="name" className="form-control"/>
                    <label htmlFor="name">Name</label>
                  </div>
                  <div className="form-floating mb-3">
                    <input onChange={this.handleFieldChange} value={this.state.color} placeholder="Color" required type="text" name="color" id="color" className="form-control"/>
                    <label htmlFor="color">color</label>
                  </div>
                  <div className="form-floating mb-3">
                    <input onChange={this.handleFieldChange} value={this.state.fabric} placeholder="fabric" required type="text" name="fabric" id="fabric" className="form-control"/>
                    <label htmlFor="fabric">Fabric</label>
                  </div>
                  <div className="form-floating mb-3">
                    <textarea onChange={this.handleFieldChange} value={this.state.style} placeholder="style" className="form-control" id="style" name="style" id="style" rows="3"></textarea>
                    <label htmlFor="style">Style</label>
                  </div>
                  <div className="form-floating mb-3">
                    <input onChange={this.handleFieldChange} value={this.state.picture_url} placeholder="picture_url" required type="text" name="picture_url" id="picture_url" className="form-control"/>
                    <label htmlFor="picture_url">Picture url</label>
                  </div>
                  <div className="mb-3">
                    <select onChange={this.handleFieldChange} value={this.state.location} required id="location" name="location" className="form-select">
                      <option value="">Choose a location</option>
                      {this.state.locations.map(location => {
                            return (
                            <option key={location.href} value={location.href}>
                                {location.closet_name}
                            </option>
                            );
                        })}

                    </select>
                  </div>
                  <button className="btn btn-primary">Create</button>
                </form>
              </div>
            </div>
          </div>
        )
    }

}

export default HatForm