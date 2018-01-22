


class Fgi_reader():

    def __init__(self,filename):
        self.filename=filename

    def fgi_read(self):
        import re
        from os.path import basename

        # self.filename = "Great UCI.txt"
        # csvfilename = "Great UCI.CSV"

        file_name = basename(self.filename).split('.')
        p1 = re.compile(r"'([0-1]+).*?")
        p2 = re.compile('bit length 32, (.*?) decimal')
        p3 = re.compile(r":([0-1]+).*?")
        p4 = re.compile('[0-1]{1}')

        k1 = 'featureGroupIndicators'
        k2 = 'featureGroupIndRel9Add'
        k3 = 'featureGroupIndRel10'
        k4 = 'bit length 32'
        f_g_i_r10 = []
        ue_cap = {file_name[0]: ''}

        with open(self.filename) as file:
            for line in file:
                if '{' in line:
                    phone_type = "iphone"
                    break
                else:
                    phone_type = 'others'
            file.seek(0)
            if phone_type != "iphone":
                p = p2
            else:
                p = p1

            for line in file:

                if k1 in line and k4 not in line and phone_type != 'iphone':
                    p = p3
                    f_g_i = p.findall(line)
                    f_g_i = f_g_i[0:32]
                elif k1 in line:
                    f_g_i = p.findall(line)
                    f_g_i = f_g_i[0:32]

                if k2 in line and k4 not in line and phone_type != 'iphone':
                    p = p3
                    f_g_i_r9 = p.findall(line)
                    f_g_i_r9 = f_g_i_r9[0:32]
                elif k2 in line:
                    f_g_i_r9 = p.findall(line)
                    f_g_i_r9 = f_g_i_r9[0:32]

                if k3 in line and k4 not in line and phone_type != 'iphone':
                    p = p3
                    if not f_g_i_r10:
                        f_g_i_r10 = p.findall(line)
                        f_g_i_r10 = f_g_i_r10[0:32]

                elif k3 in line:
                    if not f_g_i_r10:
                        f_g_i_r10 = p.findall(line)
                        f_g_i_r10 = f_g_i_r10[0:32]

        # print(f_g_i, f_g_i_r9, f_g_i_r10)
        f_g_i = p4.findall(f_g_i[0])
        f_g_i_r9 = p4.findall(f_g_i_r9[0])
        f_g_i_r10 = p4.findall(f_g_i_r10[0])

        fgi_all = f_g_i + f_g_i_r9 + f_g_i_r10

        fgi_table = [[
                     ' Intra-subframe freq hopping for PUSCH scheduled by UL grant; DCI format 3a; Aperiodic CQI/PMI/RI report on PUSCH: Mode 2-0 & 2-2 - Supported'],
                 [
                     ' Simultaneous CQI & ACK/NACK on PUCCH (format 2a/2b); Absolute TPC command for PUSCH; Resource alloc type 1 for PDSCH; Periodic CQI/PMI/RI report on PUCCH: Mode 2-0 & 2-1 - Supported'],
                 [' 5bit RLC UM SN; 7bit PDCP SN - Supported'], [' Short DRX cycle - Supported'],
                 [' Long DRX cycle; DRX command MAC control element - Supported'], [' Prioritised bit rate - Supported'],
                 [' RLC UM - Supported'], [' EUTRA RRC_CONNECTED to UTRA CELL_DCH PS handover - Supported'],
                 [' EUTRA RRC_CONNECTED to GERAN GSM_Dedicated handover - Supported'], [
                     ' EUTRA RRC_CONNECTED to GERAN (Packet_) Idle by Cell Change Order; EUTRA RRC_CONNECTED to GERAN (Packet_) Idle by Cell Change Order with NACC - Supported'],
                 [' EUTRA RRC_CONNECTED to CDMA2000 1xRTT CS Active handover - Not supported'],
                 [' EUTRA RRC_CONNECTED to CDMA2000 HRPD Active handover - Not supported'],
                 [' Inter-frequency handover (within FDD or TDD) - Supported'], [
                     ' Measurement reporting event: Event A4 - Neighbour > threshold; Measurement reporting event: Event A5 - Serving < threshold1 & Neighbour > threshold2 - Supported'],
                 [' Measurement reporting event: Event B1 - Neighbour > threshold - Supported'],
                 [' non-ANR related periodical measurement reporting - Supported'],
                 [' ANR related intra-frequency measurement reporting events - Supported'],
                 [' ANR related inter-frequency measurement reporting events - Supported'],
                 [' ANR related inter-RAT measurement reporting events - Supported'], [
                     ' SRB1 and SRB2 for DCCH + 8x AM DRB; SRB1 and SRB2 for DCCH + 5x AM DRB + 3x UM DRB (if indicator 7 is supported) - Supported'],
                 [
                     ' Predefined intra- and inter-subframe frequency hopping for PUSCH with N_sb > 1; Predefined inter-subframe frequency hopping for PUSCH with N_sb > 1 - Supported'],
                 [' UTRAN measurements, reporting and measurement reporting event B2 in E-UTRA connected mode - Supported'],
                 [' GERAN measurements, reporting and measurement reporting event B2 in E-UTRA connected mode - Supported'],
                 [
                     ' 1xRTT measurements, reporting and measurement reporting event B2 in E-UTRA connected mode - Not supported'],
                 [' Inter-frequency measurements and reporting in E-UTRA connected mode - Supported'], [
                     ' HRPD measurements, reporting and measurement reporting event B2 in E-UTRA connected mode - Not supported'],
                 [' EUTRA RRC_CONNECTED to UTRA CELL_DCH CS handover - Supported'], [' TTI bundling - Supported'],
                 [' Semi-Persistent Scheduling - Supported'], [' Handover between FDD and TDD - Supported'],
                 [' Mechanisms defined for cells broadcasting multi band information - Supported'],
                 [' Undefined - Not supported'], [' Inter-RAT ANR features for UTRAN FDD - Supported'],
                 [' Inter-RAT ANR features for GERAN - Supported'], [' Inter-RAT ANR features for 1xRTT - Not supported'],
                 [' Inter-RAT ANR features for HRPD - Not supported'],
                 [' Inter-RAT ANR features for UTRAN TDD - Not supported'],
                 [' EUTRA RRC_CONNECTED to UTRA TDD CELL_DCH PS handover - Not supported'], [
                     ' UTRAN TDD measurements, reporting and measurement reporting event B2 in E-UTRA connected mode - Not supported'],
                 [' EUTRA RRC_CONNECTED to UTRA TDD CELL_DCH CS handover - Not supported'],
                 [' Measurement reporting event: Event B1 - Neighbour > threshold for UTRAN FDD - Supported'],
                 [' Undefined - Not supported'], [' Undefined - Not supported'], [' Undefined - Not supported'],
                 [' Undefined - Not supported'], [' Undefined - Not supported'], [' Undefined - Not supported'],
                 [' Undefined - Not supported'], [' Undefined - Not supported'], [' Undefined - Not supported'],
                 [' Undefined - Not supported'], [' Undefined - Not supported'], [' Undefined - Not supported'],
                 [' Undefined - Not supported'], [' Undefined - Not supported'], [' Undefined - Not supported'],
                 [' Undefined - Not supported'], [' Undefined - Not supported'], [' Undefined - Not supported'],
                 [' Undefined - Not supported'], [' Undefined - Not supported'], [' Undefined - Not supported'],
                 [' Undefined - Not supported'], [' Undefined - Not supported'],
                 [' DMRS with OCC (orthogonal cover code) and SGH (sequence group hopping) disabling - Not supported'],
                 [' Trigger type 1 SRS (aperiodic SRS) transmission (Up to X ports) - Not supported'],
                 [' PDSCH TM9 when up to 4 CSI reference signal ports are configured - Not supported'],
                 [' PDSCH TM9 for TDD when 8 CSI reference signal ports are configured - Not supported'], [
                     ' PUCCH RM2-0 when PDSCH TM9 is configured and RM2-1 when PDSCH TM9 and up to 4 CSI reference signal ports are configured - Not supported'],
                 [' PUCCH RM2-1 when PDSCH TM9 and 8 CSI reference signal ports are configured - Not supported'], [
                     ' PUSCH RM2-0 when PDSCH TM9 is configured and RM2-2 when PDSCH TM9 and up to 4 CSI reference signal ports are configured - Not supported'],
                 [' PUSCH RM2-2 when PDSCH TM9 and 8 CSI reference signal ports are configured - Not supported'],
                 [' PUCCH RM1-1 submode 1 - Not supported'], [' PUCCH RM1-1 submode 2 - Not supported'],
                 [' Measurement reporting trigger Event A6 - Supported'],
                 [' SCell addition within the Handover to EUTRA procedure - Supported'],
                 [' Trigger type 0 SRS (periodic SRS) transmission on X Serving Cells - Not supported'],
                 [' Reporting of both UTRA CPICH RSCP and Ec/N0 in a Measurement Report - Supported'], [
                     ' Time domain ICIC RLM/RRM / ICIC RRM / ICIC CSI measurement sf restriction for the serving cell / neighbour cells - Not supported'],
                 [' Relative transmit phase continuity for spatial multiplexing in UL - Not supported'],
                 [' Undefined - Not supported'], [' Undefined - Not supported'], [' Undefined - Not supported'],
                 [' Undefined - Not supported'], [' Undefined - Not supported'], [' Undefined - Not supported'],
                 [' Undefined - Not supported'], [' Undefined - Not supported'], [' Undefined - Not supported'],
                 [' Undefined - Not supported'], [' Undefined - Not supported'], [' Undefined - Not supported'],
                 [' Undefined - Not supported'], [' Undefined - Not supported'], [' Undefined - Not supported'],
                 [' Undefined - Not supported']]

        for i, j in enumerate(fgi_all):
            if j == str(1):
                ue_cap[file_name[0]] += '\n' + fgi_table[i][0]

        return ue_cap

# example of wrting result to a csv
# for key, value in ue_cap.items():
#     print(key,value)

# import csv
#
# with open(csvfilename, 'w', newline='') as csvfile:
#     wr = csv.writer(csvfile, dialect='excel')
#     for key, value in ue_cap.items():
#         wr.writerows([[key], [value.strip()]])
# -----------------------------------------------------

# example of literate a folder
# import os
# s={}
# path = 'D:/ue_cap/'
# for filename in os.listdir(path):
#
#     s.update(Fgi_reader(os.path.join(path,filename)).fgi_read())
#     print(s.keys(),s.values())
