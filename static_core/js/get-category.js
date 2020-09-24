$(document).ready(function(){
    category=$('.dropdown-menu')
    category.empty();
    $.get('/user/category',(data)=>{
        //console.log(data);
        for(i=0;i<data.length;i++){
            category.append(
                `<li><a href="/category/${data[i].fields.slug}">${data[i].fields.name}</a></li>`);
        }
    })
});