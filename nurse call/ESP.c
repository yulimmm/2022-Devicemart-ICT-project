#include "ESP.h"

char str[] = "AT\r\n";
char echo_off[] = "ATE0\r\n";
char wifi_module[] = "AT+CWMODE=3\r\n";
char wifi_ID_PW[] = "AT+CWJAP=\"???? ??\",\"????\"\r\n";
uint8_t rx_data;
char ok[2];

void WF_initial_setting()
{
	HAL_UART_Transmit(&huart3, (uint8_t *)&str, 4, 10);
	HAL_Delay(500);
	
	HAL_UART_Transmit(&huart3, (uint8_t *)&echo_off, 6, 10);
	HAL_Delay(500);
	
	HAL_UART_Transmit(&huart3, (uint8_t *)&wifi_module, 13, 10);
	HAL_Delay(500);
	
	HAL_UART_Transmit(&huart3, (uint8_t *)&wifi_ID_PW, 4, 10);
	HAL_Delay(500);
}


void AT()
{
	HAL_UART_Transmit(&huart3, (uint8_t *)&str, 4, 10);
	HAL_Delay(500);
	HAL_UART_Transmit(&huart3, (uint8_t *)&echo_off, 6, 10);
	HAL_Delay(500);
	HAL_UART_Transmit(&huart3, (uint8_t *)&str, 4, 10);
	HAL_Delay(500);
	
	if(HAL_UART_Receive(&huart3, (uint8_t *)&ok, 4, 10)==HAL_OK)
	{
		if(ok[0]=='O' && ok[1] =='K')
		{
				HAL_GPIO_WritePin(GPIOA,GPIO_PIN_0,GPIO_PIN_SET);
				HAL_Delay(1000);
				HAL_GPIO_WritePin(GPIOA,GPIO_PIN_0,GPIO_PIN_RESET);
		}
	}


}

