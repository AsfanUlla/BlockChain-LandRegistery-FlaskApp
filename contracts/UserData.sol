pragma solidity >= 0.5.0 < 0.7.0;

contract UserData {

    string public payload;

    function setPayload(string memory content) public {
        payload = content;
    }

    function getPayload() public view returns(string memory) {
        return payload;
    }

    function sayHello() public pure returns (string memory) {
        return 'Hello';
    }
}
