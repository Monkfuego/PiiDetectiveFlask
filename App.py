import React, { useState } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import styles from './UploadForm.module.css';

function UploadForm() {
  const [file, setFile] = useState(null);
  const [results, setResults] = useState(null);  // To display results after file submission

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();

    if (!file) {
      alert("Please upload a file");
      return;
    }

    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await fetch('http://localhost:5000/upload', {
        method: 'POST',
        body: formData,
      });
      
      const result = await response.json();
      setResults(result);  // Display the results
      console.log('Response:', result);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div className={`container mt-4 ${styles.uploadFormContainer}`}>
      <div className="row">
        <div className="col-md-6 offset-md-3">
          <div className="card bg-secondary">
            <div className="card-body">
              <h5 className="card-title text-dark"><b>Upload Document</b></h5>
              <form onSubmit={handleSubmit}>
                <div className="mb-3">
                  <input 
                    type="file" 
                    className="form-control" 
                    onChange={handleFileChange} 
                  />
                </div>
                <button type="submit" className="btn btn-dark text-light">Upload</button>
              </form>

              {results && (
                <div className="mt-4">
                  <h6>Results:</h6>
                  <pre>{JSON.stringify(results, null, 2)}</pre>
                </div>
              )}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default UploadForm;
