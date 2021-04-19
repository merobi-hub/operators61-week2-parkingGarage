{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def receipt({ticket}):\n",
    "        \n",
    "    # Offer and, if prompted, create receipt with date and time\n",
    "    now = datetime.now()\n",
    "    year = now.strftime(\"%Y\")\n",
    "    month = now.strftime(\"%m\")\n",
    "    day = now.strftime(\"%d\")\n",
    "    time = now.strftime(\"%H:%M:%S\")\n",
    "    #date_time = now.strftime(\"%m/%d/%Y, %H:%M:%S\")\n",
    "                    \n",
    "    receipt_query = input('Would you like a receipt? y/n')\n",
    "    if receipt_query.lower() == 'y':\n",
    "        for k,v in removed_ticket:\n",
    "            amt = v\n",
    "        receipt = [day, time, elapsed_time, amt]\n",
    "        for i in receipt:\n",
    "            print(i)\n",
    "                    \n",
    "    # Store parking data using datetime and sqlite3\n",
    "                    \n",
    "    conn = sqlite3.connect('parking_data.sqlite')\n",
    "    cur = conn.cursor()\n",
    "        \n",
    "    cur.execute(f'INSERT INTO Parks (ticket, date, time, duration, amount) VALUES ({self.tickets[verify]}, {day}, {time}, {elapsed_time}, {amt})')"
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
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
