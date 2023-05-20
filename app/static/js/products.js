const Objects_Products = [
		{
			id: 1,
			img: "img/Placeholder.png",
			paragraph: "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod"
		},
		{
			id: 2,
			img: "img/Placeholder.png",
			paragraph: "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod"
		},
		{
			id: 3,
			img: "img/Placeholder.png",
			paragraph: "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod"
		},
		{
			id: 4,
			img: "img/Placeholder.png",
			paragraph: "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod"
		},
		{
			id: 5,
			img: "img/Placeholder.png",
			paragraph: "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod"
		},
		{
			id: 6,
			img: "img/Placeholder.png",
			paragraph: "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod"
		},
		{
			id: 7,
			img: "img/Placeholder.png",
			paragraph: "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod"
		},

	]



const ROOT_Products = document.getElementById("products");

class Products {
  render() {
    let htmlInformation = "";
    Objects_Products.forEach((element) => {
      htmlInformation += `
        <div class="product-card">
         <img class="products-img" src="${element['img']}">
         <p class="products-p">
           ${element['paragraph']}
         </p>
       </div>
      `;
      ROOT_Products.innerHTML = htmlInformation;
    });
  }
}


const products = new Products();
products.render();
