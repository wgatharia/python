## properties


class ShippingContainer:
    next_serial = 1337
    @staticmethod
    def _get_next_serial():
        result = ShippingContainer.next_serial
        ShippingContainer.next_serial += 1
        return result

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.serial = self._get_next_serial()


##test shipping container

c1 = ShippingContainer("YML", "books")
print("Owner:%s, Contents:%s, Serial: %d" % ( c1.owner_code, c1.contents, c1.serial))


c2 = ShippingContainer("MAE", "clothes")
print("Owner:%s, Contents:%s, Serial: %d" % ( c2.owner_code, c2.contents, c2.serial))



