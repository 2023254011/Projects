package com.example.awsrekognition.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class ImageChooserForm {

    @GetMapping(value = "/imagefilechooser")
    public String test() {
        return "imagefilechooser";
    }



}
