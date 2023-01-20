

def store_load():
    # Store table load

    # truncate temp table store

    # truncate_tmp_store = '''
    #                              TRUNCATE TABLE BHATBHATENI.SASHANK_TMP.TMP_STORE
    #                                  '''
    #
    # sf.execute_query(truncate_tmp_store)


    # load temp table store

    # load_tmp_store = '''
    #                        INSERT INTO BHATBHATENI.SASHANK_TMP.TMP_STORE(
    #                            STORE_ID,
    #                            RGN_KY,
    #                            STORE_DESC
    #                        )
    #                        SELECT ID,R.RGN_KY,S.STORE_DESC
    #                        FROM BHATBHATENI.SASHANK_STG.STG_STORE S
    #                        LEFT JOIN BHATBHATENI.SASHANK_TGT.TGT_REGION R
    #                        ON S.REGION_ID= R.RGN_ID
    #                        '''
    # sf.execute_query(load_tmp_store)


    # load data in   target table store


    load_tgt_store = '''
                           INSERT INTO BHATBHATENI.SASHANK_TGT.TGT_STORE(
                           LOCN_KY,LOCN_ID,
                           RGN_KY,LOCN_DESC,
                           LAST_OPEN_TMS,LAST_CLOSED_TMS,ACTV_FLG,
                           OPEN_CLOSE_CD, ROW_INSRT_TMS,ROW_UPDT_TMS
                           )
                           SELECT STORE_KY,STORE_ID,RGN_KY,STORE_DESC,LOCALTIMESTAMP,LOCALTIMESTAMP,1,1,LOCALTIMESTAMP,LOCALTIMESTAMP
                           FROM BHATBHATENI.SASHANK_TMP.TMP_STORE
                           WHERE STORE_ID NOT IN (SELECT DISTINCT LOCN_ID FROM BHATBHATENI.SASHANK_TGT.TGT_STORE)
                           '''
    sf.execute_query(load_tgt_store)


# update  target table store


    # update_tgt_store = '''
    #                            update BHATBHATENI.SASHANK_TGT.TGT_STORE as T1
    #                            set T1.RGN_KY = T2.RGN_KY ,
    #                            T1.LOCN_DESC = T2.STORE_DESC,
    #                            ROW_UDT_TMS = LOCALTIMESTAMP
    #                            FROM BHATBHATENI.SASHANK_TMP.TMP_STORE as T2
    #                            WHERE T1.LOCN_ID = T2.STORE_ID
    #                            '''
    # sf.execute_query(update_tgt_store)