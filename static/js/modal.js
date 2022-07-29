var modal;
var $project_content;


if(window_width < 992){
    $('{{ product.name }}').each(function(){
        var click = $(this).attr("onClick");
        if(click == ''){
            src = "rubik.showModal(this)";
            $(this).attr("onClick", src);
        }
    });
    
}


rubic = {
    showModal: function(button){
        var id = $(button).data('target');
        var $project = $(button).closest('{{ product.name }}');
        
        var scrollTop = $(window).scrollTop();
        var distanceTop = $project.offset().top;
    
        var projectTop = distanceTop - scrollTop; 
        var projectLeft = $project.offset().left;
        var projectHeight = $project.innerHeight();
        var projectWidth = $project.innerWidth();
    
        modal = $('#' + id);
    
        $(modal).css({
            'top'  :    projectTop,
            'left' :    projectLeft, 
            'width' :   projectWidth,
            'height' :  projectHeight,
            'z-index'  : '1032'
        });
        
        
        setTimeout(function(){
            $(modal).addClass('open');
        },30);
    
        setTimeout(function(){
            $('body').addClass('noscroll');
            $(modal).addClass('scroll');
        },1000);
    
        $('.icon-close').click(function(){
            $product.name = $(this).closest('{{ product.name }}');
            $product.name.removeClass('open scroll');
            
            $('body').removeClass("noscroll");
            //$('a').removeClass('no-opacity');
            setTimeout(function(){
                setTimeout(function(){    
                    $product.name.removeAttr('style');     
                }, 450); 
            },500);
        });
    }
}

