#include <stdbool.h>
#include <stdint.h>
#include "inc/hw_ints.h"
#include "inc/hw_memmap.h"
#include "inc/hw_types.h"
#include "inc/hw_gpio.h"
#include "inc/hw_uart.h"
#include "inc/hw_sysctl.h"
#include "driverlib/debug.h"
#include "driverlib/fpu.h"
#include "driverlib/gpio.h"
#include "driverlib/interrupt.h"
#include "driverlib/pin_map.h"
#include "driverlib/rom.h"
#include "driverlib/rom_map.h"
#include "driverlib/sysctl.h"
#include "driverlib/systick.h"
#include "driverlib/timer.h"
#include "driverlib/uart.h"
#include "driverlib/usb.h"
#include "usblib/usblib.h"
#include "usblib/usbcdc.h"
#include "usblib/usb-ids.h"
#include "usblib/device/usbdevice.h"
#include "usblib/device/usbdcdc.h"
#include "utils/ustdlib.h"
#include "usb_serial_structs.h"
#include "utils/uartstdio.h"
//

// Flags used to pass commands from interrupt context to the main loop.
//
//*****************************************************************************
#define COMMAND_PACKET_RECEIVED 0x00000001
#define COMMAND_STATUS_UPDATE   0x00000002

volatile uint32_t g_ui32Flags = 0;
char *g_pcStatus;

//*****************************************************************************
//
// Global flag indicating that a USB configuration has been set.
//
//*****************************************************************************
static volatile bool g_bUSBConfigured = false;

//*****************************************************************************
//
// Internal function prototypes.
//
//*****************************************************************************
static void GetLineCoding(tLineCoding *psLineCoding);

//*****************************************************************************
uint8_t flag=0;

void GetLineCoding(tLineCoding *psLineCoding)
{
    psLineCoding->ui32Rate =115200;
    psLineCoding->ui8Stop = USB_CDC_STOP_BITS_1;
    psLineCoding->ui8Databits = 8;
    psLineCoding->ui8Parity =USB_CDC_PARITY_NONE;
}

uint32_t ControlHandler(void *pvCBData, uint32_t ui32Event,uint32_t ui32MsgValue, void *pvMsgData)
{

    tLineCoding*MsgData=pvMsgData;
    switch(ui32Event)
    {


        case USB_EVENT_CONNECTED:
            g_bUSBConfigured = true;
            USBBufferFlush(&g_sTxBuffer);
            USBBufferFlush(&g_sRxBuffer);
            break;

        case USB_EVENT_DISCONNECTED:
            g_bUSBConfigured = false;
            break;


        case USBD_CDC_EVENT_GET_LINE_CODING:
        case USBD_CDC_EVENT_SET_LINE_CODING:
            GetLineCoding(MsgData);
            break;


        default:
            break;
    }

    return(0);
}

//*****************************************************************************



uint32_t RxHandler(void *pvCBData, uint32_t ui32Event, uint32_t ui32MsgValue,void *pvMsgData)
{
    if(ui32Event == USB_EVENT_RX_AVAILABLE)
        {

           flag=1;

        }
    return 0;
}

uint32_t TxHandler(void *pvCBData, uint32_t ui32Event, uint32_t ui32MsgValue,void *pvMsgData)
{
    return(0);
}


int main()
{
    uint8_t byte[4];
    g_bUSBConfigured = false;
    SysCtlClockSet(SYSCTL_USE_PLL|SYSCTL_OSC_MAIN|SYSCTL_XTAL_16MHZ|SYSCTL_SYSDIV_2_5);
    SysCtlPeripheralEnable(SYSCTL_PERIPH_GPIOD);
    GPIOPinTypeUSBAnalog(GPIO_PORTD_BASE, GPIO_PIN_5 | GPIO_PIN_4);
    USBBufferInit(&g_sTxBuffer);
    USBBufferInit(&g_sRxBuffer);
    USBStackModeSet(0, eUSBModeForceDevice, 0);
    USBDCDCInit(0, &g_sCDCDevice);
    IntEnable(INT_USB0);
    MAP_SysCtlPeripheralEnable(SYSCTL_PERIPH_UART0);
    MAP_SysCtlPeripheralEnable(SYSCTL_PERIPH_GPIOA);
    GPIOPinConfigure(GPIO_PA0_U0RX);
    GPIOPinConfigure(GPIO_PA1_U0TX);
    MAP_GPIOPinTypeUART(GPIO_PORTA_BASE, GPIO_PIN_0 | GPIO_PIN_1);
    MAP_UARTConfigSetExpClk(UART0_BASE, MAP_SysCtlClockGet(), 115200,
                            (UART_CONFIG_WLEN_8 | UART_CONFIG_STOP_ONE |
                             UART_CONFIG_PAR_NONE));
    //MAP_IntEnable(INT_UART0);
    //MAP_UARTIntEnable(UART0_BASE, UART_INT_RX | UART_INT_RT);

    IntMasterEnable();



    while(1)
    {
        if(flag==1)
        {
            USBBufferRead((tUSBBuffer *)&g_sRxBuffer, byte,4);
            USBBufferWrite((tUSBBuffer *)&g_sTxBuffer, byte, 4);
//            USBBufferFlush(&g_sTxBuffer);
//            USBBufferFlush(&g_sRxBuffer);
                //UARTCharPutNonBlocking(UART0_BASE, byte);
            UARTCharPutNonBlocking(UART0_BASE, byte[0]);
            UARTCharPutNonBlocking(UART0_BASE, byte[1]);
            UARTCharPutNonBlocking(UART0_BASE, byte[2]);
            UARTCharPutNonBlocking(UART0_BASE, byte[3]);

            flag=0;
        }
    }

}










