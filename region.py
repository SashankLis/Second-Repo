import Snowflake as sf


def region_load():
    #  Region table load

    # truncate tmp table region

    # truncate_tmp_region = '''
    #                              TRUNCATE TABLE BHATBHATENI.SASHANK_TMP.TMP_REGION
    #                                  '''
    #
    # sf.execute_query(truncate_tmp_region)

    # load tmp table region

    load_tmp_region = '''
                                    INSERT into BHATBHATENI.SASHANK_TMP.TMP_REGION(
                                    RGN_ID,
                                    CNTRY_KY,
                                    RGN_DESC
                                    )
                                    SELECT ID, C.CNTRY_KY, REGION_DESC
                                    FROM BHATBHATENI.SASHANK_STG.STG_REGION RGN
                                    LEFT OUTER JOIN BHATBHATENI.SASHANK_TGT.TGT_COUNTRY AS C
                                    ON RGN.COUNTRY_ID = C.CNTRY_ID
                                    '''
    sf.execute_query(load_tmp_region)



    #load data to target table region
    load_tgt_region = '''
                                INSERT INTO BHATBHATENI.SASHANK_TGT.TGT_REGION(
                                RGN_KY, RGN_ID, CNTRY_KY,
                                RGN_DESC, OPEN_CLOSE_CD,ROW_INSRT_TMS,ROW_UPDT_TMS
                                )
                                SELECT RGN_KY,RGN_ID,CNTRY_KY,RGN_DESC,1,LOCALTIMESTAMP,LOCALTIMESTAMP
                                FROM BHATBHATENI.SASHANK_TMP.TMP_REGION
                                WHERE RGN_ID NOT IN (SELECT DISTINCT RGN_ID FROM BHATBHATENI.SASHANK_TGT.TGT_REGION)
                                '''
    sf.execute_query(load_tgt_region)

    # update target table region

    # update_tgt_region = """
    #                                 update BHATBHATENI.SASHANK_TGT.TGT_REGION as T1
    #                                 set T1.RGN_DESC = T2.RGN_DESC ,
    #                                 T1.CNTRY_KY = T2.CNTRY_KY,
    #                                 ROW_UDT_TMS = LOCALTIMESTAMP
    #                                 FROM BHATBHATENI.SASHANK_TMP.TMP_REGION as T2
    #                                 WHERE T1.RGN_ID = T2.RGN_ID
    #                                 """
    #
    # sf.execute_query(update_tgt_region)

