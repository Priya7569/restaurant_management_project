<!-- templates/menu.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Restaurant Menu</title>
    </head>
    <body>
        <h1>Restaurant Menu</h1>
            <ul>
                {% for item in menu_items %}
                        <li>
                                    <h2>{{ item.name }}</h2>
                                                <p>{{ item.description }}</p>
                                                            <p>Price: {{ item.price }}</p>
                                                                        {% if item.is_available %}
                                                                                        <p>Available</p>
                                                                                                    {% else %}
                                                                                                                    <p>Not Available</p>
                                                                                                                                {% endif %}
                                                                                                                                        </li>
                                                                                                                                            {% endfor %}
                                                                                                                                                </ul>
                                                                                                                                                </body>
                                                                                                                                                </html>
                                                                                                                                                                                                                              return render(request, 'menu.html', {'menu_items': menu_items})