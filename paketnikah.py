import psycopg2

def readpaket():
    conn = psycopg2.connect(dbname="NikMate", user="postgres", password="051004", host="localhost", port="5432")
    cur = conn.cursor()
    sql = """
    SELECT p.id_paket, p.nama_paket, STRING_AGG(f.nama_fasilitas, ', '), r.nama_ruangan, p.harga_paket  
FROM detail_fasilitas_paket d 
JOIN fasilitas f ON f.id_fasilitas = d.id_fasilitas
JOIN paket_reservasi p ON p.id_paket = d.id_paket
JOIN ruangan r ON r.id_ruangan = p.id_ruangan
group by p.id_paket, r.nama_ruangan
    """    
    cur.execute(sql)
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data