from selenium import webdriver

driver = webdriver.Chrome('chromedriver')
driver.get("https://noom.typeform.com/to/xVgnbT?fbclid=IwAR0ZswVAkjV2UhoZDXl3aiQrTXJs0RvIJiDFteqoo_xPW60bWdrQO125vQc")

q1_a = driver. \
    find_element_by_xpath(
    '//*[@id="block-25b01e26-8019-4d88-a342-2023c939105b"]/div/'
    'div/div/fieldset/div[2]/div[1]/div/div[2]/div[3]/div[1]/div').click()

q1_b = driver. \
    find_element_by_xpath(
    '//*[@id="block-25b01e26-8019-4d88-a342-2023c939105b"]/div/'
    'div/div/fieldset/div[2]/div[1]/div/div[2]/div[3]/div[2]/div').click()

q1_c = driver. \
    find_element_by_xpath(
    '//*[@id="block-25b01e26-8019-4d88-a342-2023c939105b"]/div/'
    'div/div/fieldset/div[2]/div[1]/div/div[2]/div[3]/div[3]/div').click()

q1_d = driver. \
    find_element_by_xpath(
    '//*[@id="block-25b01e26-8019-4d88-a342-2023c939105b"]/div/'
    'div/div/fieldset/div[2]/div[1]/div/div[2]/div[3]/div[4]/div').click()



q2_a = driver.find_element_by_xpath('//*[@id="choice-919acc3b-5751-48e2-bf4b-af98ebc667d8"]').click()
q2_b = driver.find_element_by_xpath('//*[@id="choice-af310e64-4571-40ff-a352-252c22e20d3a"]').click()

q3_a = driver.find_element_by_xpath('//*[@id="choice-ce5ba996-6f89-46a9-a55f-ce4d3772f6f2"]').click()
q3_b = driver.find_element_by_xpath('//*[@id="choice-82f7895c-f51c-42d8-a7ac-230dab9db49c"]').click()
q3_c = driver.find_element_by_xpath('//*[@id="choice-630a6c17-ea88-414e-bac7-bfc4ec729ed6"]').click()
q3_d = driver.find_element_by_xpath('//*[@id="choice-8674c7d5-dfad-4b17-a0e8-2763811851ca"]').click()

q4_a = driver.find_element_by_xpath('//*[@id="choice-45b11614-b377-4c3c-835c-1dd82607343d"]').click()
q4_b = driver.find_element_by_xpath('//*[@id="choice-8319548e-b515-4a11-915a-bc64fb71f6f4"]').click()

q5_a = driver.find_element_by_xpath('//*[@id="choice-8674c7d5-dfad-4b17-a0e8-2763811851ca"]').click()
q5_b = driver.find_element_by_xpath('//*[@id="choice-8674c7d5-dfad-4b17-a0e8-2763811851ca"]').click()

q6_a = driver.find_element_by_xpath('//*[@id="choice-71365923-ba85-47ee-8cb0-3d0ebc338f80"]').click()
q6_b = driver.find_element_by_xpath('//*[@id="choice-10104ba2-4bd9-4a59-b962-993a6bd3bc1c"]').click()

q7_a = driver.find_element_by_xpath('//*[@id="choice-8412ed1b-74dd-4d24-8f69-d7c94d118e08"]').click()
q7_b = driver.find_element_by_xpath('//*[@id="choice-87f4726c-202d-4878-bcd9-27e647fce5c8"]').click()
q7_c = driver.find_element_by_xpath('//*[@id="choice-c16e1001-4876-41b1-9859-dd45079de0d3"]').click()

q8_a = driver.find_element_by_xpath('//*[@id="choice-4387def3-6061-42dd-abc1-1ac858465288"]').click()
q8_b = driver.find_element_by_xpath('//*[@id="choice-ec090f9a-d508-4c72-82fa-94a5eb602e42"]').click()
q8_c = driver.find_element_by_xpath('//*[@id="choice-0503b09f-00c3-44c5-be9c-c991dfea9688"]').click()

q_9_a = driver.find_element_by_id("shortText-e592fb5d-d0b5-476c-a110-a6920c0b3a1a").send_keys("python")

q10_a = driver.find_element_by_xpath('//*[@id="choice-477301be-890b-489d-85d7-a920ec18d174"]').click()
q10_b = driver.find_element_by_xpath('//*[@id="choice-8e4cd28a-a081-407c-bb13-e2a969fcdb7d"]').click()
q10_c = driver.find_element_by_xpath('//*[@id="choice-172099aa-91b8-48d7-bb0a-1137f5c8653c"]').click()

q11_a = driver.find_element_by_xpath('//*[@id="choice-17615690-a919-4378-bbe6-a624b72fa1cc"]').click()
q11_b = driver.find_element_by_xpath('//*[@id="choice-bc4e46ad-30c8-4d8c-b49b-5937451b9d22"]').click()
q11_c = driver.find_element_by_xpath('//*[@id="choice-71fe72e4-30de-44a8-9923-a2ccd50460bc"]').click()
q11_d = driver.find_element_by_xpath('//*[@id="choice-174cef05-d91a-4a1c-8914-98a6011d1c14"]').click()

q12_a = driver.find_element_by_xpath('//*[@id="choice-7254f94e-5952-49e7-ac1a-e2f70f8387ab"]').click()
q12_b = driver.find_element_by_xpath('//*[@id="choice-e021ea47-0ea6-4fb0-aae4-60ca68f09ad0"]').click()

q13_a = driver.find_element_by_xpath('//*[@id="choice-00a070fb-3c03-4377-af66-009ce76b02d2"]').click()
q13_b = driver.find_element_by_xpath('//*[@id="choice-3ac4ffc0-4f86-482f-9954-7714b8c17ad3"]').click()

q14_a = driver.find_element_by_xpath('//*[@id="choice-547e2b8b-b611-40e7-86bd-d342de2c392b"]').click()
q14_b = driver.find_element_by_xpath('//*[@id="choice-45168b9b-ecbc-45a7-bf31-6821fd492d4a"]').click()
q14_c = driver.find_element_by_xpath('//*[@id="choice-c7ac220c-1482-4829-812a-5cdb303311c9"]').click()

q15_a = driver.find_element_by_xpath('//*[@id="choice-6095e9c7-f675-4f54-8141-8029773fd173"]').click()
q15_b = driver.find_element_by_xpath('//*[@id="choice-81ff8f1d-ca7d-42be-a396-22fad14fdab4"]').click()
q15_c = driver.find_element_by_xpath('//*[@id="choice-973b9de7-ed20-43a1-95cd-4a3ac6ed7d05"]"]').click()


q16_a = driver.find_element_by_xpath('//*[@id="block-111a6113-6301-46cd-91ab-731791e179c5"]'
                                      '/div/div/div/fieldset/div[2]/div[1]/div[1]/div[2]/div[3]/div[1]/div')
q16_b = driver.find_element_by_xpath('//*[@id="block-111a6113-6301-46cd-91ab-731791e179c5"]'
                                      '/div/div/div/fieldset/div[2]/div[1]/div[1]/div[2]/div[3]/div[2]/div')
q16_c = driver.find_element_by_xpath('//*[@id="block-111a6113-6301-46cd-91ab-731791e179c5"]'
                                      '/div/div/div/fieldset/div[2]/div[1]/div[1]/div[2]/div[3]/div[3]/div')
q16_d = driver.find_element_by_xpath('//*[@id="block-111a6113-6301-46cd-91ab-731791e179c5"]'
                                      '/div/div/div/fieldset/div[2]/div[1]/div[1]/div[2]/div[3]/div[4]/div')
q16_e = driver.find_element_by_xpath('//*[@id="block-111a6113-6301-46cd-91ab-731791e179c5"]'
                                      '/div/div/div/fieldset/div[2]/div[1]/div[1]/div[2]/div[3]/div[5]/div')
q16_f = driver.find_element_by_xpath('//*[@id="block-111a6113-6301-46cd-91ab-731791e179c5"]'
                                      '/div/div/div/fieldset/div[2]/div[1]/div[1]/div[2]/div[3]/div[6]/div')
q16_g = driver.find_element_by_xpath('//*[@id="block-111a6113-6301-46cd-91ab-731791e179c5"]'
                                      '/div/div/div/fieldset/div[2]/div[1]/div[1]/div[2]/div[3]/div[7]/div')
q16_h = driver.find_element_by_xpath('//*[@id="block-111a6113-6301-46cd-91ab-731791e179c5"]'
                                      '/div/div/div/fieldset/div[2]/div[1]/div[1]/div[2]/div[3]/div[8]/div')


q1_list = [q1_a, q1_b, q1_c, q1_d]
q2_list = [q2_a, q2_b]
q3_list = [q3_a, q3_b,q3_c,q3_d]
q4_list = [q4_a, q4_b]
q5_list = [q5_a, q5_b]
q6_list = [q6_a, q6_b]
q7_list = [q7_a, q7_b, q7_c]
q8_list = [q8_a, q8_b, q8_c]

q10_list = [q10_a, q10_b, q10_c]
q11_list = [q11_a, q11_b, q11_c, q11_d]
q12_list = [q12_a, q12_b]
q13_list = [q13_a, q13_b]
q14_list = [q14_a, q14_b, q14_c]
q15_list = [q15_a, q15_b, q15_c]
q16_list = [q16_a, q16_b, q16_c, q16_d, q16_e, q16_f, q16_g, q16_h]
