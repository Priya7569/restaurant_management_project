{% for menu_item in menu_items %}
    <div>
            <h2>{{ menu_item.name }}</h2>
                    <p>{{ menu_item.description }}</p>
                            <p>Price: {{ menu_item.price }}</p>
                                    {% if menu_item.image %}
                                                <img src="{{ menu_item.image.url }}" alt="{{ menu_item.name }}">
                                                        {% else %}
                                                                    <p>No image available.</p>
                                                                            {% endif %}
                                                                                </div>
                                                                                {% endfor %}
                                                                                