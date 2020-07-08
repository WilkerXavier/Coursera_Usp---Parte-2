import time

antes = time.time()
algoritmo_a_ser_cronometrado()
depois = time.time()
print("A execusão de algoritmo demorou ", depois - antes, "segundos")