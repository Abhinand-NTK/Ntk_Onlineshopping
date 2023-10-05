const monthly_sales = JSON.parse(document.getElementById('monthly_sales').value);

console.log(monthly_sales)
console.log(monthly_sales)
console.log(monthly_sales)


const Category_Analysi_keys_input = document.getElementById('Category_Analysi_keys');
let Category_Analysi_keys = [];

if (Category_Analysi_keys_input.value) {
    Category_Analysi_keys = JSON.parse(Category_Analysi_keys_input.value);
}

console.log(Category_Analysi_keys);




const Category_Analysi_Values = JSON.parse(document.getElementById('Category_Analysi_Values').value);



console.log(Category_Analysi_Values)
console.log(Category_Analysi_Values)
console.log(Category_Analysi_Values)


const Payment_Analayis = JSON.parse(document.getElementById('Payment_Analayis').value)
console.log(Payment_Analayis)
const [a, b, c] = Payment_Analayis
console.log(a, b, c)




const ctx = document.getElementById('myChart');

new Chart(ctx, {
    type: 'polarArea',
    data: {
        labels: ['Online Payment', 'Cash On Delivery', 'Wallet Payment'],
        datasets: [{
            label: 'My First Dataset',
            data: Payment_Analayis,
            backgroundColor: [
                'rgb(255, 99, 132)',
                'rgb(75, 192, 192)',
                'rgb(255, 205, 86)',

            ]
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});

const ctx2 = document.getElementById('myChart2');

new Chart(ctx2, {
    type: 'bar',
    data: {
        labels: Category_Analysi_keys,
        datasets: [{
            label: '# of Votes',
            data: Category_Analysi_Values,
            backgroundColor: ['red', 'black', 'red', 'black', 'red', 'black', 'red', 'black', 'red', 'black', 'red', 'black'],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});




const ctx1 = document.getElementById('myChart1');

new Chart(ctx1, {
    type: 'bar',
    data: {
        labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
        datasets: [{
            label: '# of Votes',
            data: monthly_sales, // Example data for each month
            backgroundColor: [
                'rgb(255, 99, 132)',
                'rgb(75, 192, 192)',
                'rgb(255, 205, 86)',
                'rgb(54, 162, 235)',
                'rgb(153, 102, 255)',
                'rgb(255, 159, 64)',
                'rgb(255, 0, 0)',
                'rgb(0, 128, 0)',
                'rgb(128, 128, 0)',
                'rgb(0, 0, 128)',
                'rgb(128, 0, 128)',
                'rgb(128, 128, 128)'
            ], // Twelve different colors


            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});




function dataforchart() {

    const start_date_orders = document.getElementById('order_start').value;
    const end_date_orders = document.getElementById('order_end').value;



    const start_date_revenue = document.getElementById('revenue_start').value;
    const end_date_revenue = document.getElementById('revenue_end').value;

    const start_date_profit = document.getElementById('profit_start').value;
    const end_date_profit = document.getElementById('profit_end').value;


    if (start_date_orders && end_date_orders || start_date_revenue && end_date_revenue || start_date_profit && end_date_profit) {
        const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        console.log(csrfToken)

        console.log("Succeeded");

        const url = '/admin_c/totalorders/';

        // Define the data you want to send as an object, including csrfmiddlewaretoken
        const postData = {
            start_date_orders: start_date_orders,
            end_date_orders: end_date_orders,
            start_date_revenue: start_date_revenue,
            end_date_revenue: end_date_revenue,
            start_date_profit: start_date_profit,
            end_date_profit: end_date_profit,
            csrfmiddlewaretoken: csrfToken, // Include the CSRF token here
            // Add more data fields as needed
        };

        // Make the Fetch request with the headers and data
        fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json', // Specify JSON content type
                'X-CSRFToken': csrfToken, // Include CSRF token in headers as well
            },
            body: JSON.stringify(postData), // Convert the data to JSON format
        })
            .then(response => {
                // Log the response status code
                console.log('Response status:', response.status);

                // Handle the response here
                if (response.ok) {
                    return response.json() // Assuming the response is JSON
                } else {
                    throw new Error('Network response was not ok');
                }
            })
            .then(data => {
                // Process the data
                console.log(data);
                console.log(data.total_orders)


                const totalOrders = data.total_orders;
                const revenue = data.total_revenue_data;
                const profit = data.total_profit_data;

                const totalOrdersElement = document.getElementById('total_orders');
                const totalRevenueElement = document.getElementById('totalrevenue');
                const totalOrProfitElement = document.getElementById('totalprofit');

                if (totalOrdersElement) {

                    totalOrdersElement.textContent = totalOrders;

                }

                if (totalRevenueElement) {
                    if (revenue >= 0) {
                        totalRevenueElement.textContent = revenue;
                    }

                }

                if (totalOrProfitElement) {
                    if (profit >= 0) {
                        totalOrProfitElement.textContent = profit + .00;
                    }
                }



            })
            .catch(error => {
                // Handle errors
                console.error('There was a problem with the fetch operation:', error);

                // Log the response text for debugging
                error.response.text().then(text => {
                    console.error('Response text:', text);
                });
            });

    }
}

