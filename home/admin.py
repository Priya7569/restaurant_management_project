<!-- homepage.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Restaurant Homepage</title>
        <style>
                .search-container {
                            width: 80%;
                                        margin: auto;
                                                    padding: 20px;
                                                                text-align: center;
                                                                        }
                                                                                .search-bar {
                                                                                            width: 50%;
                                                                                                        padding: 10px;
                                                                                                                    font-size: 16px;
                                                                                                                                border: 1px solid #ccc;
                                                                                                                                        }
                                                                                                                                                .search-button {
                                                                                                                                                            padding: 10px 20px;
                                                                                                                                                                        font-size: 16px;
                                                                                                                                                                                    background-color: #333;
                                                                                                                                                                                                color: #fff;
                                                                                                                                                                                                            border: none;
                                                                                                                                                                                                                        cursor: pointer;
                                                                                                                                                                                                                                }
                                                                                                                                                                                                                                    </style>
                                                                                                                                                                                                                                    </head>
                                                                                                                                                                                                                                    <body>
                                                                                                                                                                                                                                        <div class="search-container">
                                                                                                                                                                                                                                                <form>
                                                                                                                                                                                                                                                            <input type="text" class="search-bar" placeholder="Search for menu items...">
                                                                                                                                                                                                                                                                        <button type="submit" class="search-button">Search</button>
                                                                                                                                                                                                                                                                                </form>
                                                                                                                                                                                                                                                                                    </div>
                                                                                                                                                                                                                                                                                    </body>
                                                                                                                                                                                                                                                                                    </html>
                                                                                                                                                                                                                                                                                                                                                                                                                          <label for=                                                                                                                                return render(request, 'menu.html', {'menu_items': menu_items})