// José Ángel Cardona García
// Graficación
// Leer el precio del producto

Proceso DescuentoDeUnProducto
	Escribir "Escribe el precio del producto: "
	Leer precio
	
	//Calcular el precio Final
	
	precio_50 <- precio * 0.5
	precio_final <- precio_50 * 0.8
	
	//Escribir el precio final
	
	Escribir "El precio final es ", precio_final
	
FinProceso
