# Jquery
Existing library to provide extra functionalit, manipulates web pages. Sits in your index with your script tag
    
    <script src="http://code.jquery.com/jquery-1.11.3.min.js"></script>

## when calling 

    $("#title").html("Goodbye");
    
    <h1 id="title">
      Hello
     </h1>
 
the dollar sign is short hand for calling a jquery function, the argument is the id selector '#title", the object being called is the page itself, or the .html, changing the html body, the arg is "goodbye", replacing the content.

# Creating Functions

    function sayHello(){
      $("#title).html("Goodbye")'
     }
## To call it

    <body>
      <h1 id="title" onClick="sayHello();">
         hello
      </h1>
    </body>
    
    <script type="text/javascript">
      function sayHello(){
         alert('hello');
        };
    </script>
    
This will call the function on the dom loading.


# Anonymous Functions

They get passed in to whatever youre calling, and never is used again. In this instance, it passes into click, changing the functionality of the button. 

        $("#title").click(function () {
            $("#title").html("Hello");
            $("#title").off("click");
         });
    
.off turns off funtionality, reverts back to the old function, returning click to whatever it did before.

    
