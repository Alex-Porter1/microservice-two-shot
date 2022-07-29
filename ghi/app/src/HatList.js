import React from 'react';
import { Link } from 'react-router-dom';

function HatColumn(props) {
    const handleDeleteClick = async haturl =>{
        const url ="http://localhost:8090"+haturl
        const fetchConfig ={
            method:'delete'
        }
    

    const response  = await fetch(url,fetchConfig);
    if(response.ok){
        window.location.reload()

    }
}



  return (
    <div className="col">
      {props.list.map(data => {
        console.log(data)
        return (
          <div key={data.href} className="card mb-3 shadow">
            <img src={data.picture_url} className="card-img-top" />
            <div className="card-body">
              <h5 className="card-title">{data.name}</h5>
              <h6 className="card-subtitle mb-2 text-muted">
                {data.fabric}--{data.color}
                <p>{data.location.name}</p>
              </h6>
              <p className="card-text">
                {data.style}
                
              </p>
            </div>
            <div className="card-footer">
            
            <button onClick={() => handleDeleteClick(data.href)} className="btn btn-primary px-4 ">Delete Hat</button>

            </div>
          </div>
        );
      })}
    </div>
  );
}





class HatList extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      hatColumns: [[], [], [],[]],
    };
  }

  async componentDidMount() {
    const url = 'http://localhost:8090/api/hats/';

    try {
      const response = await fetch(url);
      if (response.ok) {
        // Get the list of conferences
        const data = await response.json();

        // Create a list of for all the requests and
        // add all of the requests to it
        const requests = [];
        for (let hat of data.hats) {
          const detailUrl = `http://localhost:8090${hat.href}`;
          requests.push(fetch(detailUrl));
        }

        // Wait for all of the requests to finish
        // simultaneously
        const responses = await Promise.all(requests);

        // Set up the "columns" to put the conference
        // information into
        const hatColumns = [[], [], [],[]];

        // Loop over the conference detail responses and add
        // each to to the proper "column" if the response is
        // ok
        let i = 0;
        for (const hatResponse of responses) {
          if (hatResponse.ok) {
            const details = await hatResponse.json();
            hatColumns[i].push(details);
            i = i + 1;
            if (i > 3) {
              i = 0;
            }
          } else {
            console.error(hatResponse);
          }
        }

        // Set the state to the new list of three lists of
        // conferences
        this.setState({hatColumns: hatColumns});
      }
    } catch (e) {
      console.error(e);
    }
  }



  

  render() {
    return (
      <>
        <div className="px-4 py-5 my-5 mt-0 text-center bg-info">
          <img className="bg-white rounded shadow d-block mx-auto mb-4" src="https://scontent.cdninstagram.com/v/t51.29350-15/280456981_384757720331124_1529234388717912466_n.jpg?_nc_cat=107&ccb=1-7&_nc_sid=8ae9d6&_nc_ohc=TA_KLc8c3z4AX-bPe4w&_nc_ht=scontent.cdninstagram.com&edm=ANo9K5cEAAAA&oh=00_AT-oBCKvSvH36aTm6cQ3I1Tt4mZCzHmWBkBhHxxIiHGbKg&oe=62E8A36A" alt="" width="600" />
          <h1 className="display-5 fw-bold">Hats Worlds</h1>
          <div className="col-lg-6 mx-auto">
            <p className="lead mb-4">
            On he bouche le ma durant ferree. Ici affection fusillade signalant inassouvi situation ces. 
            Ca au capitaine soufflent repousser. 
            Agreerait sonnaient cartouche ii la messieurs annoncait te. Je sons cite prit ah xv. 
            </p>
            <div className="d-grid gap-2 d-sm-flex justify-content-sm-center">
              <Link to="/new" className="btn btn-primary btn-lg px-4 gap-3">Keep your hats</Link>
            </div>
          </div>
        </div>
        <div className="container">
          <h2>Your Hats</h2>
          <div className="row">
            {this.state.hatColumns.map((hatList, index) => {
              return (
                <HatColumn key={index} list={hatList} />
              );
            })}
          </div>
        </div>
      </>
    );
  }
}

export default HatList;
