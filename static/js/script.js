async function fetchData(url) {
  try {
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Error fetching data:', error);
    throw error;
  }
}

async function performSemanticSearch() {
  // Get the query input value

  const apiUrl = 'http://127.0.0.1:5000/search';
  const word = document.getElementById('query-input').value;
  
  const urlWithQueryParam = `${apiUrl}?word=${encodeURIComponent(word)}`;
    

  try {
    // Call the fetchData function and wait for the response
  const apiResult = await fetchData(urlWithQueryParam);
    console.log('API Response:', apiResult);
    const results = [];

    console.log(apiResult)
    for (let i = 0; i < apiResult.length; i++) {
      results.push({"title": apiResult[i]});
      console.log(i);
    }
    
    const resultsContainer = document.getElementById('results-container');
    resultsContainer.innerHTML = '';
    results.forEach(result => {
      const resultDiv = document.createElement('div');
      resultDiv.innerHTML = `
        <h3>${result.title}</h3>
      `;
      resultsContainer.appendChild(resultDiv);
    });
    // The code will wait here until the API request is completed.
  } catch (error) {
    // Handle errors if the API request fails.
    console.error('Something went wrong:', error);
  }


}