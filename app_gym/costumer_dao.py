from conection import Conection
from costumer import Costumer

class CostumerDAO:
    SELECT = "SELECT * FROM costumer ORDER BY id"
    INSERT = "INSERT INTO costumer(first_name, last_name, membership) VALUES(%s, %s, %s)"
    UPDATE = "UPDATE costumer SET first_name=%s, last_name=%s, membership=%s WHERE id=%s"
    DELETE = "DELETE FROM costumer WHERE id=%s"

    @classmethod
    def select(cls):
        conection = None
        try:
            conection = Conection.get_conection()
            cursor = conection.cursor()
            cursor.execute(cls.SELECT)
            records = cursor.fetchall()

            costumers = []
            for record in records:
                costumer = Costumer(record[0], record[1], record[2], record[3])
                costumers.append(costumer)
            return costumers

        except Exception as e:
            print(f"Error in select costumer: {e}")
        finally:
            if conection is not None:
                cursor.close()
                Conection.release_conection(conection)

    @classmethod
    def insert(cls, costumer):
        conection = None
        try:
            conection = Conection.get_conection()
            cursor = conection.cursor()
            values = (costumer.first_name, costumer.last_name, costumer.membership)
            cursor.execute(cls.INSERT, values)
            conection.commit()
            return cursor.rowcount


        except Exception as e:
            print(f"Error in insert costumer: {e}")
        finally:
            if conection is not None:
                cursor.close()
                Conection.release_conection(conection)

    @classmethod
    def update(cls, costumer):
        conection = None
        try:
            conection = Conection.get_conection()
            cursor = conection.cursor()
            values = (costumer.first_name, costumer.last_name, costumer.membership, costumer.id)
            cursor.execute(cls.UPDATE, values)
            conection.commit()
            return cursor.rowcount


        except Exception as e:
            print(f"Error in update costumer: {e}")
        finally:
            if conection is not None:
                cursor.close()
                Conection.release_conection(conection)

    @classmethod
    def delete(cls, costumer):
        conection = None
        try:
            conection = Conection.get_conection()
            cursor = conection.cursor()
            value = (costumer.id,)
            cursor.execute(cls.DELETE, value)
            conection.commit()
            return cursor.rowcount


        except Exception as e:
            print(f"Error in delete costumer: {e}")
        finally:
            if conection is not None:
                cursor.close()
                Conection.release_conection(conection)



if __name__ == "__main__":
    #costumer1 = Costumer(first_name="Clau", last_name="Smith", membership=255)
    #insert_costumers = CostumerDAO.insert(costumer1)
    #print(f"Inserted costumers: {insert_costumers}")

    #costumer_update = Costumer(6,"Bart", "SmSimpson", 300)
    #update_costumers = CostumerDAO.update(costumer_update)
    #print(f"Update costumers: {update_costumers}")

    costumer_delete = Costumer(id=5)
    delete_costumers = CostumerDAO.delete(costumer_delete)
    print(f"delete costumer: {delete_costumers}")

    costumers = CostumerDAO.select()
    for costumer in costumers:
        print(costumer)
