from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome("/driver/chromedriver.exe")
driver.maximize_window()
driver.get("https://www.viajesexito.com/")
# driver.find_element("/html/body/div[37]/div/div/div/div[2]/a[2]").click()
# time.sleep(6)
# driver.find_element(By.XPATH,"/html/body/div[35]/div/div/div[1]/button/span").click()
# driver.find_element(By.XPATH, "/html/body/div[38]/div/div/div/div/button").click()
#SE PARA EN LA BARRA DE BUSQUEDA
driver.find_element(By.XPATH, '/html/body/form/header/div[2]/div/div/nav/div[2]/a').click()
time.sleep(1)
#INGRESA TEXTO EN CIUDAD DE DESTINO
driver.find_element(By.XPATH, '/html/body/form/div[4]/article[1]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div[2]/div/div[1]/div/div[3]/div/div/input').send_keys("Punta Cana, Republica Dominicana (PUJ)")
time.sleep(1)
#HACE CLICK PARA ESCOGER LA FECHA
driver.find_element(By.XPATH, '/html/body/form/div[4]/article[1]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div[2]/div/div[2]/div/div[1]/div/div/input').click()
time.sleep(3)
#ESCOGE LA FECHA DE SALIDA
driver.find_element(By.XPATH, "/html/body/div[21]/div[1]/table/tbody/tr[3]/td[3]/a").click()
time.sleep(1)
#ESCOGE LA FECHA DE REGRESO
driver.find_element(By.XPATH, "/html/body/div[21]/div[1]/table/tbody/tr[4]/td[4]/a").click()
time.sleep(1)
#HACE CLICK PARA ESCOGER LOS HUESPEDES
driver.find_element(By.XPATH, '/html/body/form/div[4]/article[1]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div[2]/div/div[3]/div/div/div/div/p').click()
time.sleep(1)
#ESCOGE 3 HUESPEDES UNA SOLA HABITACION
driver.find_element(By.XPATH, '/html/body/form/div[4]/article[1]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[3]/div[1]/div[2]/div/div[3]/div/span[2]/button/span').click()
time.sleep(1)
#CLICK EN EL BOTON APLICAR
driver.find_element(By.XPATH, '/html/body/form/div[4]/article[1]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[3]/div[2]/div[2]/button').click()
time.sleep(1)
#CLICK EN EL BOTON BUSCAR
driver.find_element(By.XPATH, '/html/body/form/div[4]/article[1]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div[2]/div/div[4]/a').click()
time.sleep(10)
#OBTENER NOMBRES DE LAS AEROLINEAS
arrAerolineas = []
time.sleep(3)
for i in range(1,6):
    arrAerolineas.append(driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[2]/div/div/div[2]/div/div/div/div["+str(i)+"]/div[1]/a/span").text)
    print("----------------------- ARREGLO -------------------",arrAerolineas)
time.sleep(5)
#OBTENER TODOS LOS ELEMENTOS DE LA BUSQUEDA
print(" ----------------------------------- RESULTADOS PARA LA BUSQUEDA -----------------------------------")
for i in range(2,5):
    print(str(i-1)+") TIPO DE VUELO: ", driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[2]/div/div/div[1]/div["+str(i)+"]/a").text)
    for j in range(2,7):
        if(driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[2]/div/div/div[2]/div/div/div/div["+str(j)+"]").text != 
        " &nbsp; "):
            print("   PRECIO ["+ str(arrAerolineas[j-2]) +"] ", driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[2]/div/div/div[2]/div/div/div/div[1]/div["+str(j)+"]/a/div/div[2]/span[2]").text) 
                                                                                            # /html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[2]/div/div/div[2]/div/div/div/div[1]/div[3]/a/div/div[2]/span[2]           
#CLICK EN OPCIONES AVANZADAS                                                                                                    
driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[1]/div[1]/div/div[6]/a').click()
time.sleep(3)
#BUSCAR EN AERLINEA "AVIANCA"
driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[1]/div[1]/div/div[7]/div[2]/input').send_keys("Avianca")
time.sleep(10)
driver.quit()
