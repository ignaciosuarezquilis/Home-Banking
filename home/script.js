function mostrarResultados(informacion){
    console.log(informacion);
    let dolaroficialcompra=informacion[0].casa.compra;
    let dolaroficialventa=informacion[0].casa.venta;
    console.log(dolaroficial);
    document.getElementById('dolaroficial').innerHTML=(`Dolar oficial : ${dolaroficialcompra} ${dolaroficialventa}` );
}


function consultaCotizaciones(){
    let informacion=[];
    fetch('https://www.dolarsi.com/api/api.php?type=valoresprincipales')
        .then(response => response.json())
        .then(mostrarResultados);
}


consultaCotizaciones();