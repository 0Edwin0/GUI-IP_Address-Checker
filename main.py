import tkinter as tk
from tkinter import messagebox

import requests
from requests.exceptions import HTTPError,ConnectionError


def ip_address_status(*,format:str="json") -> requests.Response:

    """
    Gets the client's public IP address, locate and ISP details.

    Args:
        format (str, optional) : response format. Defaulr "JSON".
            Accepted values: JSON, XML, CSV.
    
    Returns:
        Response: The fetched data.

    
    Site Doc.: https://ip-api.com/docs/api:json 
    """

    api_url:str = f"http://ip-api.com/{format}"
    
    resp:requests.Response = requests.get(api_url)

    return resp


class AppUI:

    """
    GUI the Displayes the IP address, locate and ISP details.

    """

    def __init__(self,window:tk.Tk):
        self.__window = window
        self._window_height = 385
        self._window_width = 295
        
        self.__window.title("Check IP Address")
        self.__window.geometry(f"{self._window_width}x{self._window_height}")
        self.__window.wm_minsize(width=self._window_width,height=self._window_height)

        self.__layout()

        window.mainloop()

    
    def __layout(self):
        self.__window.grid_columnconfigure(0,weight=1)
        self.__window.grid_rowconfigure([0,1],weight=1)

        ui_action_frame = tk.Frame(self.__window)
        ui_action_frame.grid(row=0,column=0,padx=1,pady=1,sticky="NS")
        ui_action_frame.grid_columnconfigure(0,weight=1)
        ui_action_frame.grid_rowconfigure(0,weight=1)


        self.indicate_label = tk.Label(ui_action_frame,text=f"  {"Click ==>":>12}  ")
        self.indicate_label.grid(row=0,column=0,padx=2,pady=2,sticky="NSw")

        self.__chekc_btn = tk.Button(ui_action_frame,text="Check IP",command=self.__check_ip)
        self.__chekc_btn.grid(row=0,column=1,padx=2,pady=2,sticky="w")

        ui_details_frame = tk.Frame(self.__window)
        ui_details_frame.grid(row=1,column=0,padx=2,pady=2,sticky="NSEW")
        ui_details_frame.columnconfigure(0,weight=1)
        ui_details_frame.rowconfigure([0,1,2],weight=1)
        
        placeholder = "???"

        ## IP address Frame
            
        ip_label_frame = tk.LabelFrame(ui_details_frame,text="IP Address")
        ip_label_frame.grid(row=0,column=0,padx=2,pady=2,sticky="NSEW")
        ip_label_frame.columnconfigure(0,weight=1)
        ip_label_frame.rowconfigure([0,1],weight=1)

        tk.Label(ip_label_frame,text="IPv4").grid(
            row=0,column=0,
            padx=4,pady=4,
            sticky="NSW"
            )
        self.__ipv4_value = tk.Label(ip_label_frame,text=f"{placeholder:^50}")
        self.__ipv4_value.grid(
            row=0,column=1,
            padx=4,pady=4,
            sticky="NSW"
            )
        
        
        tk.Label(ip_label_frame,text="IPv6").grid(
            row=1,column=0,
            padx=4,pady=4,
            sticky="NSW"
            )
        self.__ipv6_value = tk.Label(ip_label_frame,text=f"{placeholder:^50}")
        self.__ipv6_value.grid(
            row=1,column=1,
            padx=4,pady=4,
            sticky="NSW"
            )
        
         ## Location info. Frame

        loc_label_frame =  tk.LabelFrame(ui_details_frame,text="Location Details")
        loc_label_frame.grid(row=1,column=0,padx=2,pady=2,sticky="NSEW")
        loc_label_frame.columnconfigure(0,weight=1)
        loc_label_frame.rowconfigure([0,1,2,3,4,5],weight=1)

        # Location info. Frame > countary

        tk.Label(loc_label_frame,text="Countary (code)").grid(
            row=0,column=0,
            padx=4,pady=4,
            sticky="NSW"
        )
        
        self.__countaryCode_label = tk.Label(loc_label_frame,text=f"{placeholder:^50}")
        self.__countaryCode_label.grid(
            row=0,column=1,
            padx=2,pady=2
        )

        # Location info. Frame > Region
        
        tk.Label(loc_label_frame,text="Region (code)").grid(
            row=1,column=0,
            padx=4,pady=4,
            sticky="NSW"
        )
        self.__regionCode_label = tk.Label(loc_label_frame,text=f"{placeholder:^50}")
        self.__regionCode_label.grid(
            row=1,column=1,
            padx=2,pady=2
        )

        # Location info. Frame > city
        tk.Label(loc_label_frame,text="City").grid(
            row=2,column=0,
            padx=2,pady=2,
            sticky="NSW"
        )
        self.__city_label = tk.Label(loc_label_frame,text=f"{placeholder:^50}")
        self.__city_label.grid(
            row=2,column=1,
            padx=2,pady=2
        )
        # Location info. Frame > PinCode
        tk.Label(loc_label_frame,text="Postal Code").grid(
            row=3,column=0,
            padx=2,pady=2,
            sticky="NSW"
        )
        self.__postal_code_label = tk.Label(loc_label_frame,text=f"{placeholder:^50}")
        self.__postal_code_label.grid(
            row=3,column=1,
            padx=2,pady=2
        )
        # Location info. Frame > Location Coordinates
        tk.Label(loc_label_frame,text="Latitude").grid(
            row=4,column=0,
            padx=2,pady=2,
            sticky="NSW"
        )
        self.__loc_lat_label = tk.Label(loc_label_frame,text=f"{placeholder:^50}")
        self.__loc_lat_label.grid(
            row=4,column=1,
            padx=2,pady=2
        )
        tk.Label(loc_label_frame,text="Longitude").grid(
            row=5,column=0,
            padx=2,pady=2,
            sticky="NSW"
        )
        self.__loc_lon_label = tk.Label(loc_label_frame,text=f"{placeholder:^50}")
        self.__loc_lon_label.grid(
            row=5,column=1,
            padx=2,pady=2
        )

        ## Network Provider info. Frame

        net_prov_label_frame =  tk.LabelFrame(ui_details_frame,text="Network Provider Details")
        net_prov_label_frame.grid(row=2,column=0,padx=2,pady=2,sticky="NSEW")
        net_prov_label_frame.columnconfigure(0,weight=1)
        net_prov_label_frame.rowconfigure([0,1],weight=1)



        tk.Label(net_prov_label_frame,text="ISP").grid(
            row=0,column=0,
            padx=2,pady=2,
            sticky="NSW"
        )
        self.__isp_label = tk.Label(net_prov_label_frame,text=f"{placeholder:^50}")
        self.__isp_label.grid(
            row=0,column=1,
            padx=2,pady=2
        )

        tk.Label(net_prov_label_frame,text="AS").grid(
            row=1,column=0,
            padx=2,pady=2,
            sticky="NSW"
        )
        self.__as_label = tk.Label(net_prov_label_frame,text=f"{placeholder:^50}")
        self.__as_label.grid(
            row=1,column=1,
            padx=2,pady=2
        )
    
    def __set_details(self,details:dict):

        if details["query"].find(".")  != -1:
            ip_addressV4 = details["query"]
            ip_addressV6 = ""
        elif details["query"].find(":")  != -1:
            ip_addressV4 = ""
            ip_addressV6 = details["query"]

        country_na_code = f"{details["country"]} ({details["countryCode"]})"
        region_na_code = f"{details["regionName"]} ({details["region"]})"
        city_na = details["city"]
        postal_code = details["zip"]
        loc_lat = details["lat"]
        loc_lon = details["lon"]
        isp = details["isp"]
        value_AS = details["as"]

        self.__ipv4_value.config(text=f"{ip_addressV4:^50}")
        self.__ipv6_value.config(text=f"{ip_addressV6:^50}")
        self.__countaryCode_label.config(text=f"{country_na_code:<50}")
        self.__regionCode_label.config(text=f"{region_na_code:<50}")
        self.__city_label.config(text=f"{city_na:<50}")
        self.__postal_code_label.config(text=f"{postal_code:<50}")
        self.__loc_lat_label.config(text=f"{loc_lat:<50}")
        self.__loc_lon_label.config(text=f"{loc_lon:<50}")
        self.__isp_label.config(text=f"{isp:<50}")
        self.__as_label.config(text=f"{value_AS:<50}")
    
    
    def __reset_details(self):
        placeholder = "---"

        self.__ipv4_value.config(text=f"{placeholder:^50}")
        self.__ipv6_value.config(text=f"{placeholder:^50}")
        self.__countaryCode_label.config(text=f"{placeholder:^50}")
        self.__regionCode_label.config(text=f"{placeholder:^50}")
        self.__city_label.config(text=f"{placeholder:^50}")
        self.__postal_code_label.config(text=f"{placeholder:^50}")
        self.__loc_lat_label.config(text=f"{placeholder:^50}")
        self.__loc_lon_label.config(text=f"{placeholder:^50}")
        self.__isp_label.config(text=f"{placeholder:^50}")
        self.__as_label.config(text=f"{placeholder:^50}")


    def __check_ip(self):

        self.indicate_label.config(text=f"< {"Checking...":^12} >")
        self.__chekc_btn.config(state=tk.DISABLED)
        self.__reset_details()
        


        def fetch_action():
            try:
                resp = ip_address_status()

                self.indicate_label.config(text=f"< {"Success":^12} >")

                resp.raise_for_status()
                r:dict = resp.json()

                self.__set_details(r)

            except HTTPError as e:
                self.indicate_label.config(text=f"< {"Failed":^12} >")
                messagebox.showerror(title="Request Error",message=e)
            except ConnectionError as e:
                self.indicate_label.config(text=f"< {"Failed":^12} >")
                messagebox.showerror(title="Connection Error",message="Failed to resolve API. Kindly check it Internet is present !")

            finally:
                self.__chekc_btn.config(state=tk.NORMAL)

        self.__window.after(500,fetch_action)    
        


if __name__ == "__main__":
    AppUI(tk.Tk())


