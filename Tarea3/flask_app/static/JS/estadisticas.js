Highcharts.chart('producto-container', {
    chart: {
      type: 'pie'
    },
    title: {
      text: 'Productos por tipo'
    },
    tooltip: {
      pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b> Cantidad: <b>({point.y})</b>'
    },
    subtitle: {
      text:
        'Source: Tarea 3 database'
    },
    plotOptions: {
      series: {
        allowPointSelect: true,
        cursor: 'pointer',
        dataLabels: [{
          enabled: true,
          distance: 20
        }, {
          enabled: true,
          distance: -40,
          format: '{point.percentage:.1f}%',
          style: {
            fontSize: '1.2em',
            textOutline: 'none',
            opacity: 0.7
          },
          filter: {
            operator: '>',
            property: 'percentage',
            value: 10
          }
        }]
      }
    },
    series: [{
      name: 'Percentage',
      colorByPoint: true,
      data: [] // Add your data here
    }],
    caption: {
      text: 'El gráfico anterior representa el número de producto por tipo.' 
    }
  });

  Highcharts.chart('pedido-container', {
    chart: {
      type: 'pie'
    },
    title: {
      text: 'Pedidos por comuna'
    },
    tooltip: {
      pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b> Cantidad: <b>({point.y})</b>'
    },
    subtitle: {
      text:
        'Source: Tarea 3 database'
    },
    plotOptions: {
      series: {
        allowPointSelect: true,
        cursor: 'pointer',
        dataLabels: [{
          enabled: true,
          distance: 20
        }, {
          enabled: true,
          distance: -40,
          format: '{point.percentage:.1f}%',
          style: {
            fontSize: '1.2em',
            textOutline: 'none',
            opacity: 0.7
          },
          filter: {
            operator: '>',
            property: 'percentage',
            value: 10
          }
        }]
      }
    },
    series: [{
      name: 'Percentage',
      colorByPoint: true,
      data: [] // Add your data here
    }],
    caption: {
      text: 'El gráfico anterior representa el número de pedidos por comuna.' 
    }
  });


  fetch("http://localhost:5000/get-estadisticas-producto")
  .then((response) => response.json())
  .then((data) => {
    
    let parsedData = data.map((item) => {
      return [
      item.tipo,
      item.cantidad];
    });

    // Get the chart by ID
    const chart = Highcharts.charts.find(
      (chart) => chart && chart.renderTo.id === "producto-container"
    );

    // Update the chart with new data
    chart.update({
      series: [
        {
          data: parsedData,
        },
      ],
    });

  })
  .catch((error) => console.error("Error:", error));  


fetch("http://localhost:5000/get-estadisticas-pedido")
.then((response) => response.json())
.then((data) => {
  let parsedData = data.map((item) => {
    return [
    item.region,
    item.cantidad];
  });
  // Get the chart by ID
  const chart = Highcharts.charts.find(
    (chart) => chart && chart.renderTo.id === "pedido-container"
  );
  // Update the chart with new data
  chart.update({
    series: [
      {
        data: parsedData,
      },
    ],
  });
})
.catch((error) => console.error("Error:", error));  