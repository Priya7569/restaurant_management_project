                                                 <!-- homepage.html -->
                                                 <!DOCTYPE html>
                                                 <html>
                                                 <head>
                                                     <title>{{ restaurant_name }}</title>
                                                         <style>
                                                                 .welcome-container {
                                                                             width: 80%;
                                                                                         margin: auto;
                                                                                                     padding: 20px;
                                                                                                                 text-align: center;
                                                                                                                         }
                                                                                                                             </style>
                                                                                                                             </head>
                                                                                                                             <body>
                                                                                                                                 <div class="welcome-container">
                                                                                                                                         <h1>Welcome to {{ restaurant_name }}</h1>
                                                                                                                                                 <p>We're glad you're here! Enjoy your dining experience with us.</p>
                                                                                                                                                     </div>
                                                                                                                                                     </body>
                                                                                                                                                     </html>
                                                                                                                                                                                                                                                                                                               <label for=                                                                                                                                return render(request, 'menu.html', {'menu_items': menu_items})