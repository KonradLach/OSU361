Investment Microservice Communication Contract


This is the communication contract for the Investment Microservice, which allows clients to programmatically request and receive data related to investment calculations. The microservice is implemented using ZeroMQ for communication between the client and the server.


Instructions for Requesting Data
To request data from the Investment Microservice, the client should follow these steps:

1: import zmq

2: Create a ZeroMQ context and socket, and connect to the microservice's address:
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

3: Prepare the data to be sent to the microservice in the form of a tuple with the following format:
(single_share_purchase_price, single_share_sold_price, total_amount_initially_invested)

4: Send the data to the microservice using send_pyobj():
collection_sent = (10, 17, 1000)  # Example data
socket.send_pyobj(collection_sent)

Instructions for Receiving Data

1: Wait for the response from the server using recv_pyobj():
result = socket.recv_pyobj()

2: The received result will be in the form of a tuple with the following format:
(per_share_gain_or_loss, percentage_gain_or_loss, investment_profit_or_loss)

Example Call


import zmq

def smta_prototype():
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    collection_sent = [
        (10, 17, 1000),
        (17, 10, 1000),
        (500, 554, 10000)
    ]

    collection_received = [
        (7, 70, 700),
        (-7, -41.176, -411.765),
        (54, 10.8, 1080)
    ]

    results = [False, False, False]

    for index in range(3):
        socket.send_pyobj(collection_sent[index])
        result = socket.recv_pyobj()
        print(result)
        results[index] = result == collection_received[index]

    return all(results)

if __name__ == '__main__':
    print('Results matched: ', smta_prototype())


![image](https://github.com/KonradLach/OSU361/assets/93342886/f4d8acdd-75da-42cb-8dc0-ecda3065f87f)


