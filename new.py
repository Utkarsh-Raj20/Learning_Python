from LinkedList import LinkedList

mon = [
    "January",
    "February",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]
months = LinkedList(mon)
months.insertAfter("February", "March")
months.printList()
