{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Bảng 'product' đã được tạo thành công (nếu chưa tồn tại).\n"
     ]
    }
   ],
   "source": [
    "import sqlite3\n",
    "\n",
    "def connect_db():\n",
    "    \"\"\"Kết nối đến cơ sở dữ liệu hoặc tạo mới nếu chưa tồn tại.\"\"\"\n",
    "    conn = sqlite3.connect(\"product.db\")  # Tên cơ sở dữ liệu\n",
    "    return conn\n",
    "\n",
    "def create_table():\n",
    "    \"\"\"Tạo bảng product trong cơ sở dữ liệu.\"\"\"\n",
    "    conn = connect_db()\n",
    "    cursor = conn.cursor()\n",
    "    cursor.execute('''\n",
    "        CREATE TABLE IF NOT EXISTS product (\n",
    "            Id INTEGER PRIMARY KEY,\n",
    "            Name TEXT NOT NULL,\n",
    "            Price REAL NOT NULL,\n",
    "            Amount INTEGER NOT NULL\n",
    "        )\n",
    "    ''')\n",
    "    conn.commit()\n",
    "    conn.close()\n",
    "    print(\"Bảng 'product' đã được tạo thành công (nếu chưa tồn tại).\")\n",
    "\n",
    "# Gọi hàm để tạo cơ sở dữ liệu và bảng\n",
    "create_table()\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.0rc1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
