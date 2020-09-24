$(document).ready(function(){
    loadingIcon()
    category=$('#category-dropdown')
    $.get('/user/category',(data)=>{
        //console.log(data)
        category.empty();
        category.append(`<option>All</option>`);
        for(i=0;i<data.length;i++){
            category.append(`<option id = "op${data[i].pk}">${data[i].fields.name}</option>`);
        }
        showArticle()
    })
})

function getCategory(){
    
}

function loadingIcon() {
    $('.pst-entry').empty();
    $('.post-entry').append(`<div class=""><img src="/static/images/rolling.gif" alt="Loading Icon" style="width:4rem; transform:translateX(500%);"></div>`)
}
function showArticle(){
    loadingIcon()
    category=$('#category-dropdown').find(":selected");
    //console.log(category.text());
    if(category.text()==='All'){
        category='All';
    }
    else{
        category=category.attr('id');
        category=category.substring(2,category.length)
    }
    
    path=window.location.pathname.split("/")
    id=path[path.length-2]
    //console.log(id);
    $.get(`/user/article?id=${id}&ctg=${category}`
            ,(data)=>{
        //console.log(data)
        $('.post-entry').empty();
        if(data.length==0){
            $('.post-entry').append(`<p>No Articles</p>`);
        }
        else{
            for(i = 0; i<data.length; i++){
                $('.post-entry').append(
                    `
                    <div class="col-md-6">
                        <div class="post">
                            <a href="/article/${data[i].fields.title_slug}/${data[i].pk}/" title="${data[i].fields.title}">
                                <img src="${data[i].fields.image}" alt="image${data[i].fields.title} - Image">
                            </a>
                            <div>
                                <h3>
                                    <a href="/article/${data[i].fields.title_slug}/${data[i].pk}/" title="${data[i].fields.title}">${data[i].fields.title}</a>
                                </h3>
                                <p>${data[i].fields.short_description}</p>
                                <span>
                                    <a href="/article/${data[i].fields.title_slug}/${data[i].pk}/" title="${data[i].fields.title}">Learn More...</a>
                                </span>
                            </div>
                        </div>
                    </div>
                    `
                )
           }
        }
       }  
    )
}