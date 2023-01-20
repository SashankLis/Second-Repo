def country_load():

    # truncate tmp table country

    # truncate_tmp_country = '''
    #                             TRUNCATE TABLE BHATBHATENI.SASHANK_TMP.TMP_COUNTRY
    #                            '''
    #
    # sf.execute_query(truncate_tmp_country)

    # load tmp table country

    load_tmp_country = """
           INSERT INTO BHATBHATENI.SASHANK_TMP.TMP_COUNTRY(
           CNTRY_ID ,
           CNTRY_DESC
            )
           SELECT ID, COUNTRY_DESC
           FROM BHATBHATENI.SASHANK_STG.STG_COUNTRY
           """

    sf.execute_query(load_tmp_country)

    #Load data to target table country

    load_tgt_country = """
        INSERT INTO BHATBHATENI.SASHANK_TGT.TGT_COUNTRY(
        CNTRY_KY ,
        CNTRY_ID ,
        CNTRY_DESC ,
        OPEN_CLOSE_CD , 
        ROW_INSRT_TMS ,
        ROW_UPDT_TMS 
        )
        SELECT CNTRY_KY, CNTRY_ID, CNTRY_DESC,1, LOCALTIMESTAMP, LOCALTIMESTAMP
        FROM BHATBHATENI.SASHANK_TMP.TMP_COUNTRY
        WHERE CNTRY_ID NOT IN (SELECT DISTINCT CNTRY_ID FROM BHATBHATENI.SASHANK_TGT.TGT_COUNTRY)
        """

    sf.execute_query(load_tgt_country)

    # Update target table country

    # update_tgt_country = """
    #                         update BHATBHATENI.SASHANK_TGT.TGT_COUNTRY as T1
    #                         set T1.CNTRY_DESC = T2.CNTRY_DESC ,
    #                         ROW_UDT_TMS = LOCALTIMESTAMP
    #                         FROM BHATBHATENI.SASHANK_TMP.TMP_COUNTRY  as T2
    #                         WHERE T1.CNTRY_ID = T2.CNTRY_ID
    #                         """
    #
    # sf.execute_query(update_tgt_country)
