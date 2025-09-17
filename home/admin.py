<form method="post" action="{% url 'login' %}">
  {% csrf_token %}
    <div>
        <label for="username">Username:</label>
            <input type="text" id="username" name="username" required>
              </div>
                <div>
                    <label for="password">Password:</label>
                        <input type="password" id="password" name="password" required>
                          </div>
                            {% if form.errors %}
                                <p style="color: red;">Invalid username or password.</p>
                                  {% endif %}
                                    <button type="submit">Login</button>
                                    </form>
                                    