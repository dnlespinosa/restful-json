const url = 'http://127.0.0.1:5000/'

function generateCupcakeHTML(cupcake) {
    return `<div id=${cupcake.id}>
                <li>${cupcake.flavor} / ${cupcake.size} / ${cupcake.rating}
                <button class='delete'>X</button>
                </li>
                <img class='img src=${cupcake.image}>
            </div>`;
}

async function showCupcakes() {
    const data = await axios.get(`${url}/cupcakes`)
    for (let cupcakeData of data.data.cupcake) {
        let cupcake  = $(generateCpcakeHTML(cupcakeData));
        $('#cupcakes-list').append(cupcake)
    }
}

$('#new-cupcakes').on('submit', async function (evt) {
    evt.preventDefault();

    let flavor = $('#flavor').val();
    let rating = $('#rating').val();
    let size = $('#size').val();
    let image = $('#image').val();

    const newCupcakeResponse = await axios.post(`${url}/cupcakes`, {
        flavor,
        rating,
        size,
        image
      });
    
      let newCupcake = $(generateCupcakeHTML(newCupcakeResponse.data.cupcake));
      $("#cupcakes-list").append(newCupcake);
      $("#new-cupcake").trigger("reset");
})

$('#cupcakes-list').on('click', '.delete', async function (evt){
    evt.preventDefault();
    let $cupcake = $(evt.target).closest('div');
    let $cupcakeId = $cupcake.attr('data-cupcake-id');

    await axios.delete(`${url}/cupcakes/${cupcakeId}`);
    $cupcake.remove
})

$(showInitialCupCakes);