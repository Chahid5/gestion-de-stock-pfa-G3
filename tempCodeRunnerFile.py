cursor.execute("UPDATE product SET name=%s, description=%s, unitprice=%f, quantity=%s, threshold=%s, datein=%s, dateout=%s WHERE product_id = %s",(self.name.text()),
        name = self.name.text()
        description = self.description.text()
        unitprice = self.unitprice.text()
        quantity = self.quantity.text()
        threshold = self.threshold.text()
        
        datein = self.datein.date().toString("yyyy-MM-dd")
        dateout = self.dateout.date().toString("yyyy-MM-dd")