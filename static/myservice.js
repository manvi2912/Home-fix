function formdisplay(id){
    let id1 = "rating_"+ id;
    let id2 = "button_rating_" + id;
    ele = document.getElementById(id1);
    ele1 = document.getElementById(id2)
    if(ele.style.display && ele1.innerText=="Give Rating"){
        ele.style.removeProperty('display');
    }
    else{
        ele.style.display= 'none';
    }
};

function reviewForm(id){
    let id1 = "reviews_"+ id;
    ele = document.getElementById(id1);
    if(ele.style.display){
        ele.style.removeProperty('display');
    }
    else{
        ele.style.display= 'none';
    }
}