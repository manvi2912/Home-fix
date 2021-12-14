function change(id){
    let id1 = "s_"+id;
    let id2 = "change_"+id;
    console.log(document.getElementById(id2));
    console.log(document.getElementById(id1));
    if(document.getElementById(id2).style.display){
             document.getElementById(id2).style.removeProperty('display');
             document.getElementById(id1).style.display= 'none';
    }
    else{
             document.getElementById(id1).style.removeProperty('display');
             document.getElementById(id2).style.display= 'none';
    }
}