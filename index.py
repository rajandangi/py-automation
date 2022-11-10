from datetime import datetime, timedelta
import os
import errno
import csv
from Database import Database


def exporter():
    with Database() as db:
        now = datetime.now()
        pastdate = now - timedelta(days=1)
        currentdate = now.strftime("%Y%b%d_%H%M%S")
        pastDate = pastdate.strftime("%Y-%m-%d")
        bankIds = db.query(
            """select distinct (bank_id) from bank_details_table order by bank_id asc""")

        # export CSV
        print("CSV Created at =", currentdate)
        for bankId in bankIds:
            transactionSql = "select b.id,b.batch_id,b.rec_date,b.batch_amount,batch_chrg_amount,batch_crncy," \
                             "debtor_agent ,Debtor_branch, debtor_name ,debtor_account , debtor_mobile , " \
                             "debtor_email,channel_id, debit_status ,b.rcre_user_id,b.settlement_date,session_srl_no " \
                             ",b.iso_txn_id,t.id ,t.instruction_id, end_to_end_id , app_id ,app_txn_id,creditor_agent " \
                             ",creditor_branch , creditor_name , creditor_account ,credit_status,ref_id,remarks ," \
                             "particulars,free_code_1,free_code_2,t.free_text_1,t.addenda1,t.addenda2,t.addenda3," \
                             "t.addenda4 from cips_batch_detail_table b,cips_transaction_detail_table t where " \
                             "b.id=t.batch_id and b.debit_status !='ENTR'and b.debtor_agent='" + \
                             bankId[0] + "' and b.settlement_date='" + \
                             pastDate + "'"
            results = db.query(transactionSql)
            directory = "D:\\data\\" + bankId[0] + "\\"
            if not os.path.exists(os.path.dirname(directory)):
                try:
                    os.makedirs(os.path.dirname(directory))
                except OSError as exc:  # Guard against race condition
                    if exc.errno != errno.EEXIST:
                        raise
            # print(sql_query)
            filename = directory + bankId[0] + currentdate + "connectIps.csv"
            with open(filename, 'w', encoding="utf-8") as csvFile:
                # Extract the table headers.
                headers = ['NCHL Batch id', 'Input Batch Id', 'Trans. Date', 'Batch Amount', 'Charge Amount',
                           'Currency',
                           'Debtor Bank Code', 'Debtor Branch', 'Debtor Name', 'Debtor Account', 'Debtor Mobile',
                           'Debtor Email', 'Channel Type', 'Debit Status', 'UserName', 'Settlement Date',
                           'Session Sequence', 'Debit ISO Id', 'NCHL Trans. Id', 'Instruction Id', 'EndtoEndId',
                           'Application Id',
                           'APPTXNID', 'Creditor Bank Code', 'Creditor Branch Code', 'Creditor Name',
                           'Creditor Account',
                           'Credit Status', 'Reference Id', 'Remarks', 'Tran Particulars']
                # Create CSV writer.
                writer = csv.writer(csvFile, delimiter=',', lineterminator='\r',
                                    quoting=csv.QUOTE_ALL, escapechar='\\')
                # Add the headers and data to the CSV file.
                writer.writerow(headers)
                writer.writerows(results)
