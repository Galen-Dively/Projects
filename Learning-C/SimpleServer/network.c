#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>

#define PORT 8080
#define BUFFER_SIZE 1024

void server()
{
    int server_fd, new_socket, len;
    struct sockaddr_in address;
    int addrLen = sizeof(address);
    char buffer[BUFFER_SIZE] = {0};
    char *response = "Hello client";


    // Assign Varibalies with no error handling
    server_fd = socket(AF_INET, SOCK_STREAM, 0);

    address.sin_port = htons(PORT);
    address.sin_family = AF_INET;
    address.sin_addr.s_addr = INADDR_ANY; 

    bind(server_fd, (struct sockaddr *)&address, addrLen);

    listen(server_fd, 5);

    new_socket = accept(server_fd, (struct sockaddr *)&address, (socklen_t *)&addrLen);

    int valread = read(new_socket, buffer, BUFFER_SIZE);
    printf("Client says: %d valread", buffer);

     // Send a response to the client
    send(new_socket, response, strlen(response), 0);
    printf("Response sent to client.\n");

    // Close the sockets
    close(new_socket);
    close(server_fd);


}

void client()
{
    int sockD = socket(AF_INET)
}

int main()
{
    printf("Program ran");
    return 1;
}