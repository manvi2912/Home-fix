function allReview(service_id, index){
    console.log(document.getElementById(service_id))
    if(document.getElementById(service_id).style.display){
             document.getElementById(service_id).style.removeProperty('display');
             document.getElementById(index).innerHTML = `<span class="click">Hide Reviews</span>`;
    }
    else{
        document.getElementById(service_id).style.display= 'none';
        document.getElementById(index).innerHTML = `<span class="click">Read Reviews</span>`;
    }
}