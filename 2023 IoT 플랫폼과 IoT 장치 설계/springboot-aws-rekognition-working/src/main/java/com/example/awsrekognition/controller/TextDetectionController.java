package com.example.awsrekognition.controller;
/*
import com.amazonaws.services.rekognition.AmazonRekognition;
import com.amazonaws.services.rekognition.AmazonRekognitionClientBuilder;
import com.amazonaws.services.rekognition.model.*;
import com.example.awsrekognition.service.AwsRekognitionService;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

import java.util.List;

@Controller
public class TextDetectionController {

    private AwsRekognitionService awsRekognitionService;

    public TextDetectionController(AwsRekognitionService awsRekognitionService) {
        this.awsRekognitionService = awsRekognitionService;
    }


    @GetMapping("detecttext")
    public String detecttext(Model model) {

        String resultString = "";
        String photo = "ocrtestimage.jpg";
        String bucket = "photo-collection2";

        //AmazonRekognition rekognitionClient = AmazonRekognitionClientBuilder.defaultClient();
        AmazonRekognition rekognitionClient = awsRekognitionService.returnClient();


        DetectTextRequest request = new DetectTextRequest()
                .withImage(new Image()
                        .withS3Object(new S3Object()
                                .withName(photo)
                                .withBucket(bucket)));


        try {
            DetectTextResult result = rekognitionClient.detectText(request);
            List<TextDetection> textDetections = result.getTextDetections();

            System.out.println("Detected lines and words for " + photo);
            for (TextDetection text: textDetections) {

                System.out.println("Detected: " + text.getDetectedText());
                resultString = resultString + text.getDetectedText();

                System.out.println("Confidence: " + text.getConfidence().toString());
                System.out.println("Id : " + text.getId());
                System.out.println("Parent Id: " + text.getParentId());
                System.out.println("Type: " + text.getType());
                System.out.println();

            }
        } catch(AmazonRekognitionException e) {
            e.printStackTrace();
        }

        model.addAttribute("textdetectionresult", resultString);

        return "textdetection";
    }


}
 */
